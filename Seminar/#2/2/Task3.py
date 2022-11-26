import re

string = input("Введите текст >> ")
poisk = input("Строка поиска >> ")
count = 0

count = len(re.findall(poisk, string))

# printing result
print(f"Строка {poisk} встречается {str(count)} раз ")

