from AccessControl.unauthorized import Unauthorized
from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.config import KEY_USEFUL, KEY_COMMENT,\
    KEY_DATE, KEY_IP, FORM_FIELD_USEFUL, FORM_FIELD_COMMENT
from collective.wasthisuseful.event import UsefulnessEvent
from collective.wasthisuseful.interfaces import IUsefulnessManager
from DateTime import DateTime
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from zope.component import getMultiAdapter
import zope.event


class FormParserView(BrowserView):
    """Parse the submitted "was this useful"-form.
    """

    def _createVote(self, useful, comment=None):
        now = DateTime()
        useful_int = int(useful)
        vote = {
            KEY_USEFUL: useful_int,
            KEY_COMMENT: comment,
            KEY_DATE: now,
            KEY_IP: self.request.getClientAddr(),
            }
        return vote

    def _addVote(self, vote):
        manager = IUsefulnessManager(self.context)
        votes = manager.getVotes()
        votes.append(vote)
        manager.setVotes(votes)
        event = UsefulnessEvent(self.context)
        zope.event.notify(event)
        self.messages.addStatusMessage(_(u'message_thank_you',
                                         default=u'Thank you for voting!'))

    def __call__(self):
        self.messages = IStatusMessage(self.request)
        form = self.request.form
        authenticator = getMultiAdapter(
            (self.context, self.request), name=u"authenticator")

        if not form or FORM_FIELD_USEFUL not in form:
            self.messages.addStatusMessage('No form submitted.')
        elif not authenticator.verify():
            raise Unauthorized
        else:
            vote = self._createVote(form[FORM_FIELD_USEFUL],
                                    comment=form.get(FORM_FIELD_COMMENT, None))
            self._addVote(vote)
        self.request.RESPONSE.redirect(self.context.absolute_url())
