from typing import List
from typing import Callable
from typing import Dict

from transport_tycoon.domain.event import DomainEvent
from typing_extensions import Type


class EventManager:

    def __init__(self) -> None:
        self.subscribers: Dict[Type[DomainEvent], List[Callable[[DomainEvent], None]]] = {}
        self.events: List[DomainEvent] = []

    def record(self, event: DomainEvent) -> None:
        self.events.append(event)
        for subscriber in self.subscribers.get(event.__class__, []):
            subscriber(event)

    def subscribe_for(self, event_type: Type[DomainEvent], subscriptor: Callable[[DomainEvent], None]) -> None:
        self.subscribers[event_type] = [subscriptor]
