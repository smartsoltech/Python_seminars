quater = int(input("Введите номер четверти >> "))

if quater == 1:
    print("x > 0 (до бесконечности), y > 0 (до бесконечности)")
elif quater == 2:
    print("x < 0 (до бесконечности), y > 0 (до бесконечности)")
elif quater == 3:
    print("x < 0 (до бесконечности), y < 0 (до бесконечности)")
elif quater == 4:
    print("x < 0 (до бесконечности), y < 0 (до бесконечности)")
else:
    print("Не верный ввод!")
