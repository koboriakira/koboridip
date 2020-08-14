import csv
from typing import List
from koboridip.calculator import Printer


class CsvPrinter(Printer):
    def print(self, add, subtract, multiply, divide) -> None:
        result: List[List] = []
        result.append(["add", add])
        result.append(["subtract", subtract])
        result.append(["multiply", multiply])
        result.append(["divide", divide])

        with open('result.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)
