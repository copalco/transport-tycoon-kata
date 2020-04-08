import unittest
from typing import Optional

from transport_tycoon.domain.cargo_delivered import CargoDelivered
from transport_tycoon.domain.event import DomainEvent
from transport_tycoon.events.event_manager import EventManager


class TestEventManager(unittest.TestCase):

    def test_emits_events(self) -> None:
        manager = EventManager()
        manager.record(CargoDelivered())
        self.assertEqual(manager.events, [CargoDelivered()])

    def test_subscribers_can_listen_for_specified_events(self) -> None:
        subscriber = FakeDeliveredSubcriber()
        manager = EventManager()
        manager.subscribe_for(CargoDelivered, subscriber.handle_cargo_delivered)
        manager.record(CargoDelivered())
        self.assertEqual(subscriber.received, CargoDelivered())


class FakeDeliveredSubcriber:

    def __init__(self) -> None:
        self.received: Optional[CargoDelivered] = None

    def handle_cargo_delivered(self, event: DomainEvent) -> None:
        self.received = event
