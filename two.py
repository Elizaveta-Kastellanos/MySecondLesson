# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. (умножаем на -3)

n = int(input('Введите число: '))
i = 1
count = 0
num_list = []
while count < n:
    num_list.append(str(i))
    # print(i, end=',')
    i *= -3       # i = i * (-3)
    count += 1    # count = count + 1  
print(",".join(num_list))              
