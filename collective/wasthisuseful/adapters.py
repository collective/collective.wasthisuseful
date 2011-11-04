from zope.annotation.interfaces import IAnnotations
from zope.component import adapts 
 
from Products.CMFCore.interfaces import IContentish

from plone.stringinterp import _ as PloneStringInterpMessageFactory
from plone.stringinterp.adapters import BaseSubstitution
from plone.stringinterp.interfaces import IStringSubstitution 

from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.config import KEY_USEFUL, KEY_COMMENT, \
                                                                    STORAGE_KEY

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
