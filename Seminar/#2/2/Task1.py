#Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#    
#    *Пример:*
#    - Для N = 5: 1, -3, 9, -27, 81

n = int(input("Введите число >> "))

if n < 0:
    print("Введено число меньше нуля!")
else: 
    while a < n:
        
        #print('Цикл выполнился', a, 'раз(а)')
        num = num*(-3)
        a = a+1
        print(f'{n} : {num}')
    
