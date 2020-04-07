from typing import List

from transport_tycoon.events.event import Event


class EventManager:

    def __init__(self) -> None:
        self.events: List[Event] = []

    def record(self, event: Event) -> None:
        self.events.append(event)
