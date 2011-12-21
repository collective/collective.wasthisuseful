from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility 
 
from plone.registry.interfaces import IRegistry
from plone.stringinterp import _ as PloneStringInterpMessageFactory
from plone.stringinterp.adapters import BaseSubstitution

from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.config import KEY_USEFUL, KEY_COMMENT, \
                                  STORAGE_KEY, SETTINGS_KEY, CHILDREN_ENABLED, \
                                  ITEM_ENABLED
from collective.wasthisuseful.interfaces import IWasThisUsefulSettings

class usefulnessRatingCommentSubstitution(BaseSubstitution):
    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_comment', default=u'Comment')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_comment = manager.getVotes()[-1].get(KEY_COMMENT)
        return last_vote_comment

class usefulnessRatingValueSubstitution(BaseSubstitution):
    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_value', default=u'Rating')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_value = manager.getVotes()[-1].get(KEY_USEFUL)
        if last_vote_value:
            value = 'Yes'
        else:
            value = 'No'
        return value

class UsefulnessManager(object):
    """See interfaces.py, IUsefulnessManager
    """

    def __init__(self, context):
        self.context = context

    def getVotes(self):
        return IAnnotations(self.context).get(STORAGE_KEY, [])

    def setVotes(self, votes):
        IAnnotations(self.context)[STORAGE_KEY] = votes

class UsefulnessSettingsManager(object):
    """See interfaces.py, IUsefulnessSettingsManager

    Settings are stored as a dictionary.
    """

    def __init__(self, context):
        self.context = context

    def getSettings(self):
        return IAnnotations(self.context).get(SETTINGS_KEY, {})

    def getParentSettings(self):
        return IAnnotations(self.context.aq_parent).get(SETTINGS_KEY, {})

    def setSettings(self, settings):
        IAnnotations(self.context)[SETTINGS_KEY] = settings

    def delSettings(self, settings, context=None):
        if not context:
            context = self.context
        del(IAnnotations(context)[SETTINGS_KEY])
        
    def delRating(self, key, context):
        if not context:
            context = self.context
        if SETTINGS_KEY in IAnnotations(context) and key in IAnnotations(context)[SETTINGS_KEY]:
            del(IAnnotations(context)[SETTINGS_KEY][key])
        
    def disableRating(self, children=False):
        """Disable rating for item and or its children
        """
        settings = self.getSettings()
        
        if children:
            settings.update({CHILDREN_ENABLED: False})
            
            # Remove ITEM_ENABLED from children, but keep CHILDREN_ENABLED
            for item in self.context.listFolderContents():
                self.delRating(ITEM_ENABLED, item)
            
        settings.update({ITEM_ENABLED: False})
        self.setSettings(settings)

    def enableRating(self, children=False):
        """Enable rating for item and or its children
        """
        settings = self.getSettings()
        
        if children:
            settings.update({CHILDREN_ENABLED: True})
            
            # Remove ITEM_ENABLED from children, but keep CHILDREN_ENABLED
            for item in self.context.listFolderContents():
                self.delRating(ITEM_ENABLED, item)
            
        settings.update({ITEM_ENABLED: True})
        self.setSettings(settings)

    def ratingEnabledType(self):
        """Check if type is enabled
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWasThisUsefulSettings)
        enabled_types = settings.enabled_types
        
        return self.context.portal_type in enabled_types

    def ratingEnabled(self):
        """Check if rating is enabled on object
        """
        
        settings = self.getSettings() 
        value = False
        
        if settings and ITEM_ENABLED in settings:
            value = settings[ITEM_ENABLED]
        else:
            parent_settings = self.getParentSettings()
            if parent_settings:
                value = CHILDREN_ENABLED in parent_settings and parent_settings[CHILDREN_ENABLED]
            else:
                value = self.ratingEnabledType
                
        return value

    def childrenEnabled(self):
        """Check if rating is enabled for this element's children
        """

        settings = self.getSettings()
        value = False
        
        if self.context.isPrincipiaFolderish and settings and CHILDREN_ENABLED in settings:
            value = settings[CHILDREN_ENABLED]
            
        return value