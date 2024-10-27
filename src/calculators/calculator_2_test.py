
from .calculator_2 import Calculator2
from typing import Dict
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'Calculator': 2, 'Result': 0.08}}
