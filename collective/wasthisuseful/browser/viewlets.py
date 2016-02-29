from collective.wasthisuseful.interfaces import IUsefulnessSettingsManager
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.wasthisuseful.browser.views.wasthisusefulform import\
    UsefulForm, NotUsefulForm


class WasThisUsefulViewlet(ViewletBase):
    render = ViewPageTemplateFile('useful.pt')

    def update(self):
        self.enabled = self._isEnabledType()

    def _isEnabledType(self):
        manager = IUsefulnessSettingsManager(self.context)
        return manager.ratingEnabled()

    def get_not_useful_form(self):
        """ Get the form, updated, so we can render it """
        form = NotUsefulForm(self.context, self.request)
        form.update()
        return form

    def get_useful_form(self):
        """ Get the form, updated, so we can render it """
        form = UsefulForm(self.context, self.request)
        form.update()
        return form
