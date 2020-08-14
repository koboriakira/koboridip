from koboridip.csv_printer import CsvPrinter
import sys
from koboridip.calculator import Calculator, Printer
from koboridip.json_printer import JsonPrinter
from koboridip.simple_printer import SimplePrinter

if __name__ == '__main__':
    # 引数を取得
    a = sys.argv[1]
    b = sys.argv[2]
    # 出力方式
    mode = sys.argv[3]

    # Printerクラスを指定
    printer: Printer = JsonPrinter() if mode == 'json' else CsvPrinter(
    ) if mode == 'csv' else SimplePrinter()

    # Calculatorインスタンスを作成
    calculator = Calculator(int(a), int(b), printer)

    # 四則演算の結果をそれぞれ出力
    calculator.print()
