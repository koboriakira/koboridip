import json
from typing import Dict
from koboridip.calculator import Printer


class JsonPrinter(Printer):
    def print(self, add, subtract, multiply, divide) -> None:
        result: Dict[str, int] = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }
        with open('result.json', mode='w') as f:
            f.write(json.dumps(result))
