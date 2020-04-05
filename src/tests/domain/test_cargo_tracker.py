import unittest

from transport_tycoon.tracker import CargoTracker
from transport_tycoon.domain.cargo_loaded import CargoLoaded


class TestCargoTracker(unittest.TestCase):

    def test_knows_when_cargo_was_loaded_on_vehicle(self) -> None:
        tracker = CargoTracker()
        tracker.loaded()
        assert tracker.events == [CargoLoaded()]
