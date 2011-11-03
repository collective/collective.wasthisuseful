from zope.annotation.interfaces import IAnnotations

from collective.wasthisuseful.config import STORAGE_KEY

class UsefulnessManager(object):
    """
    """

    def __init__(self, context):
        self.context = context

    def getVotes(self):
        return IAnnotations(self.context).get(STORAGE_KEY, [])

    def setVotes(self, votes):
        IAnnotations(self.context)[STORAGE_KEY] = votes


