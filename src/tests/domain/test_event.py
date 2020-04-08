import unittest

from transport_tycoon.domain.event import DomainEvent


class TestDomainEvent(unittest.TestCase):

    def test_descendants_are_equal_if_class_is_the_same(self) -> None:
        class One(DomainEvent):
            pass

        class Different(DomainEvent):
            pass

        self.assertEqual(One(), One())
        self.assertNotEqual(One(), Different())
