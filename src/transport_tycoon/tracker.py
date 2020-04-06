import typing

from transport_tycoon.domain.cargo_loaded import CargoLoaded


class CargoTracker:

    def __init__(self) -> None:
        self.events: typing.List[CargoLoaded] = []

    def loaded(self) -> None:
        self.events.append(CargoLoaded())
