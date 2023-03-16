import unittest
from creational.singleton import Singleton


class TestSingletonClass(unittest.TestCase):
    def test_singleton(self):
        s1 = Singleton()
        s2 = Singleton()

        self.assertIs(s1, s2)
