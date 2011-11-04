from zope.component import getMultiAdapter, getUtility

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry

from collective.wasthisuseful.interfaces import IWasThisUsefulSettings

class WasThisUsefulViewlet(ViewletBase):
    render = ViewPageTemplateFile('useful.pt')

    def update(self):
        self.enabled = self._isEnabledType()
        pass

    def _isEnabledType(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWasThisUsefulSettings)
        enabled_types = settings.enabled_types
        return self.context.portal_type in enabled_types
