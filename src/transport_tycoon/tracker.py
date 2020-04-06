import typing

from transport_tycoon.domain.cargo_delivered import CargoDelivered
from transport_tycoon.domain.cargo_loaded import CargoLoaded


class CargoTracker:

    def __init__(self) -> None:
        self.events: typing.List[typing.Union[CargoLoaded, CargoDelivered]] = []

    def cargo_has_been_loaded(self) -> None:
        self.events.append(CargoLoaded())

    def cargo_has_been_delivered(self) -> None:
        self.events.append(CargoDelivered())
