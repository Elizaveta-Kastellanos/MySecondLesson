
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

try:
    n = int(input('Введите целое число: '))
    multiplicate_list = []
    tmp = 1
    for i in range(1, n+1):
        i *= tmp
        multiplicate_list.append(i)
        tmp = i
    print(multiplicate_list)
except ValueError: 
    print('Вы ввели не целое число')

# 3.) !!! третье задание как мы обговаривали с вами , я не делала по примеру 
# для n = 6: (1:4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19)

try:
    n = int(input('Введите целое число: '))
    sum_new_list = []
    tmp = 1
    for i in range(1, n+1):
        tmp += 3
        sum_new_list.append(tmp)
    print(sum_new_list)
    i = tmp
except ValueError: 
    print('Вы ввели не целое число')

# 4.) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#     Найдите произведение элементов на указанных позициях.
#     Позиции хранятся в файле file.txt в одной строке одно число.
import random
from random import randint

try:
    MY_FILE = 'file_txt'
    n_elem = int(input('Введите N: '))
    n_elems = [random.randint(-n_elem, n_elem) for i in range(n_elem)]
    print(n_elems)
    write_positions = open(MY_FILE, 'w')
    for i in range(0, n_elem):
        i = str(i)
        write_positions.write(f'{i}\n')
    write_positions.close()
    data_multiplication_position = open(MY_FILE, 'r')
    positions = []
    product_of_numbers = 1
    for i in data_multiplication_position:
        i = int(i)
        elem = n_elems[i]
        product_of_numbers *= elem
    print(product_of_numbers)

    # 5.) Реализуйте алгоритм перемешивания списка. Reverse.
    #     !!Список взят из задания номер 4 (т.е. из предыдущего)

    my_reverse_list = []
    my_index = len(n_elems)
    while my_index > 0:
        my_reverse_list.append(n_elems[my_index-1])
        my_index = my_index - 1
    print(my_reverse_list)
except ValueError:
    print('Упс. Введи целое число')













