def my_func(num_1:int, num_2:int, num_3:int):
    """функция принимает три аргумента и возвращает сумму наибольших двух"""
    my_list = [num_1, num_2, num_3]
    return sum(my_list) - min(my_list)
print("Здравствуйте! Ведите пожалуйста 3 числа и мы посчитаем сумму двух\
  наибольших из них для Вас.")

while True:
    try:
        num_1 = int(input("Пожалуйста введите первое число: "))
        num_2 = int(input("Пожалуйста введите второе число: "))
        num_3 = int(input("Пожалуйста введите третье число: "))
    except ValueError:
        print("Пожалуйста вводите цифры!!!")
    else:
        print(f"Ваша сумма: {my_func(num_1, num_2, num_3)}")
        break