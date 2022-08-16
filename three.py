# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

first_str = input('Введите текст, который ищем: ') # 
second_str = input('Введите текст, в котором ищем: ') # 
count = 0
while first_str in second_str:
    tmp = second_str.find(first_str)
    count += 1
    if second_str == first_str:
        break
    second_str = second_str[tmp + len(first_str):]
print(count)
    

   




