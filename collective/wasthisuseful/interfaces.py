from zope import schema
from zope.interface import Interface

from collective.wasthisuseful import wasthisusefulMessageFactory as _

class IWasThisUsefulProductLayer(Interface):
    """Marker interface for browser layer
    """

class IUsefulnessManager(Interface):
    """Helper class to update votes
    """
    def getVotes():
        """Get the list of all votes
        """
    def setVotes():
        """Re-set the list of all votes
        """

class IUsefulnessSettingsManager(Interface):
    """Helper class to manage settings for object: can it be rated.
    """
    def ratingEnabled():
        """
        """

class IWasThisUsefulSettings(Interface):
    """Global settings for "Was this useful". 
	This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    enabled_types = schema.Tuple(
		title=_(u'label_enabled_types', default=u'Enabled types'),
		description=_(u"help_enabled_types",
				   default=u"For which content types shall we enable rating?"),
		required=False,
		default=('Document',),
		value_type=schema.Choice(
						vocabulary="plone.app.vocabularies.UserFriendlyTypes"),
		)
