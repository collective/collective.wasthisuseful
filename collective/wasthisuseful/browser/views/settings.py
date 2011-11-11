from Products.Five import BrowserView

from collective.wasthisuseful.interfaces import IUsefulnessManager

class UsefulnessSettingsView(BrowserView):
    """Management screen for individual objects.

    - ratings enabled yes/no
    - possibly later: rating details (date, IP)
    """
    
    def ratingEnabled(self):
        manager = IUsefulnessManager(self.context)
        return manager.ratingEnabled()
        
