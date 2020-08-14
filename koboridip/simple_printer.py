from koboridip.calculator import Printer


class SimplePrinter(Printer):
    def print(self, add, subtract, multiply, divide) -> None:
        print(f'add: {add}')
        print(f'subtract: {subtract}')
        print(f'multiply: {multiply}')
        print(f'divide: {divide}')
