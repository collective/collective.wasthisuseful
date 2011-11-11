from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from collective.wasthisuseful.interfaces import IUsefulnessSettingsManager

class WasThisUsefulViewlet(ViewletBase):
    render = ViewPageTemplateFile('useful.pt')

    def update(self):
        self.enabled = self._isEnabledType()

    def _isEnabledType(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.ratingEnabled()
