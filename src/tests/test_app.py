import unittest

from transport_tycoon.app.transport_tycoon import TransportTycoonApp


class TestTransportTycoonApp(unittest.TestCase):

    def test_cargo_delivery_to_warehouse_b_takes_five_time_units(self) -> None:
        app = TransportTycoonApp()
        app.deliver(cargo=[])
