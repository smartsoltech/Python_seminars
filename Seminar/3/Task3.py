a = int(input("Введите 1 число >> "))
b = int(input("Введите 2 число >> "))


def NOK(a,b):
    i = min(a, b)
    print('i = ', i)
    while True:
        if i%a==0 and i%b==0:
            break
        i += 1
    return i

print(NOK(a,b))