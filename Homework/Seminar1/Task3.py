#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка. ⋀ - and ⋁ - or ¬ - not

x = int(input("Введите X >> "))
y = int(input("Введите Y >> "))

if (x>0) and (y>0):
    print("1 quater")
elif (x<0) and (y>0):
    print ("2 quater")
elif (x<0) and (y<0):
    print ("3 quater")
elif (x>0) and (y>0):
    print ("4 quater")

        
        