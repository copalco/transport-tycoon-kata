import typing

from transport_tycoon.tracker import CargoTracker


class TransportTycoonApp:

    def __init__(self) -> None:
        self.cargo_tracker = CargoTracker()

    def deliver(self, cargo: typing.List[str]) -> typing.Optional[int]:
        if not cargo:
            return 0
        for item in cargo:
            self.cargo_tracker.register()
        return None
