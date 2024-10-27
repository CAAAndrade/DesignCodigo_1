import numpy as np
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self._np = np

    def standard_deviation(self, numbers: List[float]) -> float:
        return self._np.std(numbers)