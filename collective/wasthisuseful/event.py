from zope.component.interfaces import ObjectEvent, IObjectEvent
from zope.interface import implements

class IUsefulnessEvent(IObjectEvent):
    """An item has been rated for usefulness"""

class UsefulnessEvent(ObjectEvent):
    """
    """
    implements(IUsefulnessEvent)

