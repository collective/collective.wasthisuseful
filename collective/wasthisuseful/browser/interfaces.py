#from plonetheme.classic.browser.interfaces import IThemeSpecific \
#                                                               as IClassicTheme
#class IThemeSpecific(IClassicTheme):
#    """theme-specific layer"""

from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface
    """

