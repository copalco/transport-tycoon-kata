from typing import List, Callable, Dict, Tuple

from transport_tycoon.domain.event import DomainEvent
from typing_extensions import Type


class EventManager:

    def __init__(self) -> None:
        self.subscribers: Dict[Type[DomainEvent], Callable[[DomainEvent], None]] = {}
        self.events: List[DomainEvent] = []

    def record(self, event: DomainEvent) -> None:
        self.events.append(event)

    def subscribe_for(self, event_type: Type[DomainEvent], subscriptor: Callable[[DomainEvent], None]) -> None:
        self.subscribers[event_type] = subscriptor
