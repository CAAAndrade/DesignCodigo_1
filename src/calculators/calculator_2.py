"""
Segunda Calculadora
* N numeros são enviados.
* Todos esses N numeros são multiplicados por 11 e elevados a potencia de 0.95.
* Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor
(l/result)
Dica: Utilize a lib Numpy para calcular o desvio padrão

"""

from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator2:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self._driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)

        formatted_response = self.__format_response(calculated_number)

        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            # verifica se o body enviado pelo cliente contem o campo 'numbers'
            raise Exception("body is badly formatted")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self._driver_handler.standard_deviation(first_process_result)
        return 1/result

    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "Result": round(calculated_number, 2),
            }
        }