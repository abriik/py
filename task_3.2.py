def user_data(name, second_name, born, city, email, mobile_number):
    """Функция принимает данные о пользователе и выводит их одной строкой."""
    print(f"Пользователь {name} {second_name} {born} года рождения, проживает в городе {city}. Контактные данные пользователя: почта - {email},\
  и номер мобильного телефона - {mobile_number}")

name = input("Пожалуйста введите своё имя: ")
second_name = input("Пожалуйста введите свою фамилию: ")
born = input("Пожалуйста введите год своего рождения: ")
city = input("Пожалуйста введите название города в котором Вы проживаете: ")
email = input("Пожалуйста введите свою электронну почту: ")
mobile_number = input("Пожалуйста введите свой номер мобильного телефона: ")

user_data(mobile_number = mobile_number, born = born, name = name,
          email = email, second_name = second_name, city = city)