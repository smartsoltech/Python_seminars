num = int(input("Введите число >> "))
if (num < 1) or (num > 7):
    print("Введенное число не соответствует ни одному дню недели")
elif num < 6:
    print("Это будний день!")
else:
    print("Выходной! УРААААА")
    