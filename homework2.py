
# 1.) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23, - 0,56 -> 11


try:
    num_str = input('Введите любое число: ')
    sum = 0
    for i in num_str:
        if i == ',' or i == '.':
            i = 0
        i = int(i)
        if i >= -9 and i <= 9:
            sum += i
    print(sum)
except ValueError:
    print('Вы ввели не число!')



# 2.) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 


# try:
#     n = int(input('Введите целое число: '))
#     multiplicate_list = []
#     tmp = 1
#     for i in range(1, n+1):
#         i *= tmp
#         multiplicate_list.append(i)
#         tmp = i
#     print(multiplicate_list)
# except ValueError: 
#     print('Вы ввели не целое число')







