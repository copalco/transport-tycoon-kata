import unittest

from transport_tycoon.domain.cargo_delivered import CargoDelivered
from transport_tycoon.tracker import CargoTracker
from transport_tycoon.domain.cargo_loaded import CargoLoaded


class TestCargoTracker(unittest.TestCase):

    def test_no_cargo_registered(self) -> None:
        tracker = CargoTracker()
        self.assertEqual(tracker.registered, 0)

    def test_knows_when_cargo_was_loaded_on_vehicle(self) -> None:
        tracker = CargoTracker()
        tracker.cargo_has_been_loaded()
        assert tracker.events == [CargoLoaded()]

    def test_knows_when_cargo_has_been_delivered(self) -> None:
        tracker = CargoTracker()
        tracker.cargo_has_been_delivered()
        self.assertEqual(tracker.events, [CargoDelivered()])
