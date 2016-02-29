from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.config import STORAGE_KEY, SETTINGS_KEY,\
    CHILDREN_ENABLED, ITEM_ENABLED
from collective.wasthisuseful.interfaces import IWasThisUsefulSettings
from plone.registry.interfaces import IRegistry
from plone.stringinterp import _ as PloneStringInterpMessageFactory
from plone.stringinterp.adapters import BaseSubstitution
from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility


class usefulnessRatingCommentSubstitution(BaseSubstitution):
    """ Subsitution for the commenter's comment """
    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_comment', default=u'Comment')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_comment = manager.getLatestVote().get('comment')
        return last_vote_comment


class usefulnessRatingValueSubstitution(BaseSubstitution):
    """ Subsitution for the commenter's vote """
    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_value', default=u'Rating')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_value = manager.getLatestVote().get('useful')
        if last_vote_value:
            value = 'Yes'
        else:
            value = 'No'
        return value


class usefulnessRatingEmailSubstitution(BaseSubstitution):
    """ Subsitution for the commenter's e-mail """
    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_email', default=u'E-mail')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_email = manager.getLatestVote().get('email')
        return last_vote_email


class UsefulnessManager(object):
    """See interfaces.py, IUsefulnessManager
    """

    def __init__(self, context):
        self.context = context

    def getVotes(self):
        return IAnnotations(self.context).get(STORAGE_KEY, [])

    def setVotes(self, votes):
        IAnnotations(self.context)[STORAGE_KEY] = votes

    def addVote(self, vote):
        """ Add the vote """
        votes = self.getVotes()
        votes.append(vote)
        self.setVotes(votes)

    def getLatestVote(self):
        """ Get the latest vote """
        votes = self.getVotes()
        if votes:
            return votes[-1]
        return {}


class UsefulnessSettingsManager(object):
    """See interfaces.py, IUsefulnessSettingsManager

    Settings are stored as a dictionary.
    """

    def __init__(self, context):
        self.context = context

    def getSettings(self, parent=False):
        context = self.context
        if parent:
            context = context.aq_parent
        return IAnnotations(context).get(SETTINGS_KEY, {})

    def setSettings(self, settings):
        IAnnotations(self.context)[SETTINGS_KEY] = settings

    def delSettings(self, settings, context=None):
        if not context:
            context = self.context
        del(IAnnotations(context)[SETTINGS_KEY])

    def delRating(self, key, context):
        if not context:
            context = self.context
        if SETTINGS_KEY in IAnnotations(context) and\
           key in IAnnotations(context)[SETTINGS_KEY]:
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
            parent_settings = self.getSettings(parent=True)
            if parent_settings:
                value = parent_settings.get(CHILDREN_ENABLED, None)
            else:
                value = self.ratingEnabledType

        return value

    def childrenEnabled(self):
        """Check if rating is enabled for this element's children
        """

        settings = self.getSettings()
        value = False

        if self.context.isPrincipiaFolderish and CHILDREN_ENABLED in settings:
            value = settings[CHILDREN_ENABLED]

        return value
