#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = (input("Введите число: "))
a = int(number + number)
b = int(number + number + number)
sum = int(number) + a + b
print(sum)
#total = (n + int(str(n) + str(n)) + int(str(n) + str(n)))
#print("Сумма чисел n + nn + nn - %d % total")
