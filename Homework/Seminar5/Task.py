txt = input("Введите текст:")
print(f" Введенный текст: {txt}")
find_txt = input('Введите строку, которую надо удалить >> ')
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')