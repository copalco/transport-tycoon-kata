import unittest

from transport_tycoon.events.event_manager import EventManager


class TestEventManager(unittest.TestCase):

    def test_emits_events(self) -> None:
        EventManager()
