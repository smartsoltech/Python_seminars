def input_numbers(x): 
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        reality = False
        while not reality:
            try:
                number = int(input(f"Введите координату {xy[i]}: "))
                a.append(number)
                reality = True
            except ValueError:
                print("Введите целое число")
    return a


def Length(a, b):  
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
    return lengthSegment


print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Длина отрезка: {round(Length(pointA, pointB),2)}")
