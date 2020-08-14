from abc import ABCMeta, abstractmethod


class Calculator():
    def __init__(self, a: int, b: int, printer) -> None:
        self.a = a
        self.b = b
        self.printer = printer

    def print(self) -> None:
        add = self.a + self.b
        subtract = self.a - self.b
        multiply = self.a * self.b
        divide = self.a / self.b
        self.printer.print(add, subtract, multiply, divide)


class Printer(metaclass=ABCMeta):
    @abstractmethod
    def print(self, add, subtract, multiply, divide):
        pass
