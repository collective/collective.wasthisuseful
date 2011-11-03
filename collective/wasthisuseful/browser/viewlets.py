from zope.component import getMultiAdapter

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class WasThisUsefulViewlet(ViewletBase):
    render = ViewPageTemplateFile('useful.pt')

    def update(self):
        pass
