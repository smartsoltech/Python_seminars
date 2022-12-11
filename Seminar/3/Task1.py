with open('file_Task1.txt', 'r') as f:
    string = f.read()
print(string)

array = string.split(' ')
min = min(array)
max = max(array)

print(f'Минимум - {min}, Максимум - {max}')