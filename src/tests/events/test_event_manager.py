import unittest

from transport_tycoon.domain.cargo_delivered import CargoDelivered
from transport_tycoon.events.event import Event
from transport_tycoon.events.event_manager import EventManager


class TestEventManager(unittest.TestCase):

    def test_emits_events(self) -> None:
        manager = EventManager()
        manager.record(Event())
        self.assertEqual(manager.events, [Event()])

    def test_subscribers_can_listen_for_specified_events(self) -> None:
        manager = EventManager()
        manager.subscribe_for(CargoDelivered())
