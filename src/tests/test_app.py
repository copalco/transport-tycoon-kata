import unittest

from transport_tycoon.app.transport_tycoon import TransportTycoonApp


class TestTransportTycoonApp(unittest.TestCase):

    def test_delivering_no_cargo_takes_no_time(self) -> None:
        app = TransportTycoonApp()
        self.assertEqual(app.deliver(cargo=[]), 0)
