
from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriver:
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3

# testa a integração entre o driver(NumpyHandler) e o calculador


def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'Calculator': 2, 'Result': 0.08}}


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriver()
    calculator_2 = Calculator2(driver)

    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'Calculator': 2, 'Result': 0.33}}
