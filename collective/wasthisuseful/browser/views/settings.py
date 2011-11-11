from Products.Five import BrowserView

from collective.wasthisuseful.interfaces import IUsefulnessSettingsManager

class UsefulnessSettingsView(BrowserView):
    """Management screen for individual objects.

    - ratings enabled yes/no
    - possibly later: rating details (date, IP)
    """
    
    def ratingEnabled(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.ratingEnabled()
