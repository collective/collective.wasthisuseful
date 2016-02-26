from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.interfaces import IUsefulnessSettingsManager
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage


class UsefulnessSettingsView(BrowserView):
    """Management screen for individual objects.

    - ratings enabled yes/no
    - possibly later: rating details (date, IP)
    """

    @property
    def ratingEnabled(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.ratingEnabled()

    @property
    def childrenEnabled(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.childrenEnabled()

    @property
    def isFolderish(self):
        return self.context.isPrincipiaFolderish

    def processForm(self):
        form = self.request.form
        messages = IStatusMessage(self.request)
        if form:
            manager = IUsefulnessSettingsManager(self.context)
            if 'disable_rating' in form:
                manager.disableRating()
                messages.addStatusMessage(
                    _(u'Rating was disabled for this object'))
            elif 'disable_rating_children' in form:
                manager.disableRating(children=True)
                messages.addStatusMessage(
                    _(u'Rating was disabled for this object and its children'))
            elif 'enable_rating' in form:
                manager.enableRating()
                messages.addStatusMessage(
                    _(u'Rating was enabled for this object'))
            elif 'enable_rating_children' in form:
                manager.enableRating(children=True)
                messages.addStatusMessage(
                    _(u'Rating was enabled for this object and its children'))

            self.request.RESPONSE.redirect(self.request.URL)
        else:
            # no form submitted, do nothing
            pass
