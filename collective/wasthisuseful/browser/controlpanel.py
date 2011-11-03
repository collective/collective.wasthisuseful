from plone.app.registry.browser import controlpanel

from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.interfaces import IWasThisUsefulSettings


class WasThisUsefulSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IWasThisUsefulSettings
    label = _(u"Was This Useful settings")
    description = _(u"""""")

    def updateFields(self):
        super(WasThisUsefulSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(WasThisUsefulSettingsEditForm, self).updateWidgets()

class WasThisUsefulSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = WasThisUsefulSettingsEditForm
