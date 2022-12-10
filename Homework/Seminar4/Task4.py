#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import itertools
from random import randint

k = int(input('Введите степень '))

def random_numbers(k):
    numbers = [randint(0,100) for i in range(k)]
    while numbers[0] == 0:
        numbers[0] = randint(1, 10)
    return numbers

def urov(k, numbers):
    f = ['*x^']*(k-1) + ['*x']
    cheekibreeki = [[a, b, c] for a, b, c in itertools.zip_longest(numbers, f, range(k, 1, -1), fillvalue= '') if a != 0]
    for x in cheekibreeki:
        x.append(' + ')
    cheekibreeki = list(itertools.chain(*cheekibreeki))
    cheekibreeki[-1] = ' = 0'
    return "".join(map(str, cheekibreeki)).replace(' 1*x', ' x')
numbers = random_numbers(k)
check_list = urov(k, numbers)
print(check_list)

with open('./Homework/Seminar4/text.txt', 'w') as data:
    data.write(check_list)