import unittest
from typing import Optional

from transport_tycoon.domain.cargo_delivered import CargoDelivered
from transport_tycoon.domain.cargo_loaded import CargoLoaded
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

    def test_subscribers_for_similar_event_will_both_get_id(self) -> None:
        first_subscriber = FakeDeliveredSubcriber()
        second_subscriber = FakeDeliveredSubcriber()
        manager = EventManager()
        manager.subscribe_for(CargoDelivered, first_subscriber.handle_cargo_delivered)
        manager.subscribe_for(CargoDelivered, second_subscriber.handle_cargo_delivered)
        manager.record(CargoDelivered())
        self.assertEqual(first_subscriber.received, CargoDelivered())
        self.assertEqual(second_subscriber.received, CargoDelivered())

    def test_subscriber_wont_get_event_it_does_not_listen_for(self) -> None:
        first_subscriber = FakeDeliveredSubcriber()
        second_subscriber = FakeDeliveredSubcriber()
        manager = EventManager()
        manager.subscribe_for(CargoDelivered, first_subscriber.handle_cargo_delivered)
        manager.subscribe_for(CargoLoaded, second_subscriber.handle_cargo_delivered)
        manager.record(CargoDelivered())
        self.assertEqual(first_subscriber.received, CargoDelivered())
        self.assertIsNone(second_subscriber.received)


class FakeDeliveredSubcriber:

    def __init__(self) -> None:
        self.received: Optional[CargoDelivered] = None

    def handle_cargo_delivered(self, event: DomainEvent) -> None:
        self.received = event
