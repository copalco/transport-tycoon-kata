import unittest

from transport_tycoon.app.transport_tycoon import TransportTycoonApp


class TestTransportTycoonApp(unittest.TestCase):

    def test_delivering_no_cargo_takes_no_time(self) -> None:
        app = TransportTycoonApp()
        self.assertEqual(app.deliver(cargo=[]), 0)

    def test_cargo_is_registered(self) -> None:
        app = TransportTycoonApp()
        app.deliver(cargo=['B', 'A', 'B'])
        self.assertEqual(app.cargo_tracker.registered, 3)

    @unittest.expectedFailure
    def test_calculates_delivery_of_cargo_to_warehouse_b(self) -> None:
        app = TransportTycoonApp()
        self.assertEqual(app.deliver(cargo=['B']), 5)
