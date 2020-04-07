from typing import List

from transport_tycoon.domain.cargo_delivered import CargoDelivered
from transport_tycoon.events.event import Event


class EventManager:

    def __init__(self) -> None:
        self.events: List[Event] = []

    def record(self, event: Event) -> None:
        self.events.append(event)

    def subscribe_for(self, event: CargoDelivered) -> None:
        pass
