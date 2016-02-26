from collective.wasthisuseful.interfaces import IUsefulnessSettingsManager
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class WasThisUsefulViewlet(ViewletBase):
    render = ViewPageTemplateFile('useful.pt')

    def update(self):
        self.enabled = self._isEnabledType()

    def _isEnabledType(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.ratingEnabled()
