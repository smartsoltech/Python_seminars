#Вычислить число c заданной точностью d
#Пример:
#- при d = 0.001, π = 3.141   
#Ввод: 0.01
#    Вывод: 3.14#

#    Ввод: 0.001
#    Вывод: 3.141
import math
from cmath import pi

accuracy = input('Введите точность в формате 0.001 >> ').split('.')
#print(f'Разоранная на кортеж строка ввода: {accuracy}')
value = accuracy[1]
#print(f'Второй элемент кортежа {value}')
k = 0
for i in range(len(value)):
    if int(value[i]) == 0:
        k += 1
#print(f' количество нулей после запятой - {k}')       
print(f'Значение числа  Pi c точностью "{accuracy[0]}.{accuracy[1]}" равно {round(pi, k)}')
