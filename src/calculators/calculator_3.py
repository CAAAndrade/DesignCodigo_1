'''
    Calculadora 3
        * N numeros são colocados como entrada
        * Caso a variância de todos esses numeros for menor que a
        multiplicação deles, é apresentado uma informação de sucesso ao
        usuario.
        * Caso contrário, é apresentado uma informação de falha.
    Obs: Para o calculo de variância, utilize o método "var" da lib numpy
'''
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List, Dict
from src.drivers.numpy_handler import NumpyHandler
from flask import request as FlaskRequest


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self._driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_results(variance, multiplication)

        return self.__format_response(multiplication)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            # verifica se o body enviado pelo cliente contem o campo 'numbers'
            raise Exception("body is badly formatted")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self._driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for number in numbers:
            multiplication *= number
        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception(
                "Falha no processo. Variância menor que a multiplicação")

    def __format_response(self, variance: float) -> Dict:
        return {"data": {"Calculator": 3, "value": variance, "success": True}}
