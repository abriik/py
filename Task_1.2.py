#Пользователь вводит время в секундах.
# Переведите время в часы, минуты,
# секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input("Введите время в секндах: "))
hours = user_time // 3600
residue = user_time % 3600
minutes = residue // 60
sec = residue % 60
print(f"Сейчас {hours}:{minutes}:{sec} ")