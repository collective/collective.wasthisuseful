from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage

from collective.wasthisuseful.interfaces import IUsefulnessSettingsManager
from collective.wasthisuseful import wasthisusefulMessageFactory as _

class UsefulnessSettingsView(BrowserView):
    """Management screen for individual objects.

    - ratings enabled yes/no
    - possibly later: rating details (date, IP)
    """
    
    def ratingEnabled(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.ratingEnabled()
    
    def isFolderish(self):
        return self.context.isPrincipiaFolderish

    def processForm(self):
        form = self.request.form
        messages = IStatusMessage(self.request)
        if form:
            manager = IUsefulnessSettingsManager(self.context)
            if form.has_key('disable_rating'):
                manager.disableRating()
                messages.addStatusMessage(_(u'message_disabled',
                    default=u'Rating was disabled for this object and its children.'))
            else:
                if form.has_key('enable_rating'):
                    manager.enableRating()
                    messages.addStatusMessage(_(u'message_enabled',
                        default=u'Rating was enabled for this object and its children.'))
            self.request.RESPONSE.redirect(self.request.URL)
        else:
            # no form submitted, do nothing
            pass
        
