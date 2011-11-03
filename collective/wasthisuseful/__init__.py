from zope.i18nmessageid import MessageFactory

wasthisusefulMessageFactory = MessageFactory('collective.wasthisuseful')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
