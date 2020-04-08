import abc

import typing


class DomainEvent(abc.ABC):

    def __eq__(self, other: typing.Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return True
