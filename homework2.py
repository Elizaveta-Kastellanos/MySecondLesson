
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23, - 0,56 -> 11



num_str = input('Введите любое число: ')
sum = 0
for i in num_str:
    if i == ',' or i == '.':
        i = 0
    try:
        i = int(i)
    except ValueError:
        print('Вы ввели не число!')
        break
    if i >= -9 and i <= 9:
        sum = sum + i
print(sum)









