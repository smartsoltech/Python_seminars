from random import randint, shuffle

lst = [i for i in range(10)]

for i in range(len(lst)):
    temp = lst[i]
    r = randint(0, len(lst) - 1)
    lst[i] = lst[r]
    lst[r] = temp
print(lst)