# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input("Enter time in seconds: "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
sec = (time_in_seconds % 3600) % 60
print(f"The time is: {hours}:{minutes}:{sec} ")
