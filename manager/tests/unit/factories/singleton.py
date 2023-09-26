from factories.singleton import Singleton
from unittest import TestCase
from unittest.mock import MagicMock


def init_mock_instance() -> dict[str, str]:
    return {"hello": "world", "testing": "singleton"}


class TestSingleton(TestCase):
    def setUp(self) -> None:
        self.init_mock_instance = MagicMock(wraps=init_mock_instance)
        self.singleton = Singleton(self.init_mock_instance)

    def test_should_init_and_return_instance_on_first_call(self) -> None:
        instance = self.singleton.get()
        self.assertEqual(instance, init_mock_instance())
        self.init_mock_instance.assert_called_once()

    def test_should_only_init_the_instance_once(self) -> None:
        instance1 = self.singleton.get()
        instance2 = self.singleton.get()
        self.init_mock_instance.assert_called_once()
        self.assertIs(instance1, instance2)
