from typing import List, Callable, Dict

from transport_tycoon.domain.cargo_delivered import CargoDelivered


class EventManager:

    def __init__(self) -> None:
        self.subscribers: Dict[CargoDelivered, Callable[[CargoDelivered], None]] = {}
        self.events: List[CargoDelivered] = []

    def record(self, event: CargoDelivered) -> None:
        self.events.append(event)

    def subscribe_for(self, event: CargoDelivered, subscriptor: Callable[[CargoDelivered], None]) -> None:
        self.subscribers[event] = subscriptor
