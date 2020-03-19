# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class ZeroDiv:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def zero_div(divider, denominator):
        try:
            return divider / denominator
        except:
            return f"Деление на ноль недопустимо"


div = ZeroDiv(10, 100)
print(ZeroDiv.zero_div(10, 0))
print(ZeroDiv.zero_div(10, 0.1))
print(div.zero_div(100, 0))
