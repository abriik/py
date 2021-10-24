#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


seasons_list = [
    ['зима', ['12', '1', '2']],
    ['весна', ['3', '4', '5']],
    ['лето', ['6', '7', '8']],
    ['осень', ['9', '10', '11']]
]

seasons_dict = {
    'зима': ['12', '1', '2'],
    'весна': ['3', '4', '5'],
    'лето': ['6', '7', '8'],
    'осень': ['9', '10', '11']
}

while True:
    month_number = input('Напишите номер месяца: ')
    if month_number not in sum(seasons_dict.values(), []):
        print('Вы неправильно ввели номер месяца. Попробуйте еще раз')
        continue

    break

for season, months in seasons_list:
    if month_number in months:
        print(f'В списке месяц под номером {month_number} , значит это {season}')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'В словаре месяц с номером {month_number} , значит это {season}')

