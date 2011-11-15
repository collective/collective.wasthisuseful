from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility 
 
from plone.registry.interfaces import IRegistry
from plone.stringinterp import _ as PloneStringInterpMessageFactory
from plone.stringinterp.adapters import BaseSubstitution

from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.config import KEY_USEFUL, KEY_COMMENT, \
                                  STORAGE_KEY, SETTINGS_KEY, ENABLE_CHILDREN
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

    def disableRating(self):
        """Disable rating for item and its children
        """
        settings = self.getSettings()
        settings.update({ENABLE_CHILDREN: False})
        self.setSettings(settings)

    def enableRating(self):
        """Enable rating for item and its children
        """
        settings = self.getSettings()
        settings.update({ENABLE_CHILDREN: True})
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
        if settings:
            value = settings[ENABLE_CHILDREN]
        else:
            parent_settings = self.getParentSettings()
            if parent_settings:
                value = parent_settings[ENABLE_CHILDREN]
            else:
                value = self.ratingEnabledType
        return value
