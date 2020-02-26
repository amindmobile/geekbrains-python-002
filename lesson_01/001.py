# поработайте с переменными, создайте несколько, выведите на экран,
# запросите от пользователя и сохраните в переменную, выведите на экран

integer_ = 5
float_ = 2.7
string_ = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
tuple_ = (1, 'Lorem ipsum dolor', ('tuple in tuple', 'some text'))
list_ = [1, 'Lorem ipsum dolor', {'dict in list', }, ['list in list']]
dictionary_ = {
    1: 'Lorem ipsum dolor',
    'ключ': 'значение',
    'two': ['list in dict'],
    ('tuple as key', ): ('tuple in dict', ),
    'dict': {'dict in dict'}
}
print(f'Ниже следуют примеры переменных в ЯП Python:')
print(f'Целое число: "{integer_}"')
print(f'Число с плавающей точкой: "{float_}"')
print(f'Строка: "{string_}"')
print(f'Кортеж: "{tuple_}"')
print(f'Список: "{list_}"')
print(f'Словарь: "{dictionary_}"')

user_input = input('Enter here anything: ')
print(f'You are entered: {user_input}')
