from abc import ABC
from typing import List


class Good:
    """
    Товар
    """
    name: str
    cost: float


class ReceiptItem:
    """
    Элемент чека, содержит информацию о товаре, его количестве и стоимости
    """
    good: Good
    cost: float
    quantity: float
    amount_cost: float


class Receipt:
    """
    Чек, содержит список проданных товаров, итоговую стоимость, представляет инструменты для вывода данных
    """
    items: List[ReceiptItem]
    summary_cost: float

    def print(self):
        job = PrintJob()
        job.print(*self.items, summary_cost=self.summary_cost)


class Printer(ABC):
    """
    Абстрактный класс устройства для вывода чеков
    """
    def print(self, *args, **kwargs):
        pass


class ReceiptPrinter(Printer):
    """
    Чековый принтер
    """
    def print(self, *args, **kwargs):
        self.send_to_receipt_printer(*args, **kwargs)

    def send_to_receipt_printer(self, *args, **kwargs):
        pass


class SimplePrinter(Printer):
    """
    Обычный принтер
    """
    def print(self, *args, **kwargs):
        self.send_to_simple_printer(*args, **kwargs)

    def send_to_simple_printer(self, *args, **kwargs):
        pass


class EmailPrinter(Printer):
    """
    Отправка по email
    """
    def print(self, *args, **kwargs):
        print('Not implemented yet')
        pass


class PrintJob:
    """
    Задание для вывода чека существующими способами
    """
    print_ways = [ReceiptPrinter, SimplePrinter, ]

    def print(self, *args, **kwargs):
        for way in self.print_ways:
            printer = way()
            printer.print(*args, **kwargs)
