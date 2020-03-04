# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(**kwargs):
    return ", ".join(kwargs.values())


print(user_info(user_first_name="Добрыня",
                user_last_name="Таргариен",
                user_birth_year="1539",
                user_city="Rostov",
                user_email="d.targarien@beresta.rus",
                user_phone="5(700)211-41-11",
                ))
