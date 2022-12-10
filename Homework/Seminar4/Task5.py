from itertools import chain
import itertools
import re

file1 = './Homework/Seminar4/text1.txt'
file2 = './Homework/Seminar4/text2.txt'
file_sum = './Homework/Seminar4/sum.txt'


def read_file(file):
    with open(str(file), 'r') as data:
        text = data.read()
    print(text)
    return text


def convert_file(text):
    text = text.replace('= 0', '')
    text = re.sub("[*|^| ]", " ", text).split('+')
    text = [char.split(' ') for char in text]
    text = [[x for x in list if x] for list in text]
    for i in text:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    text = [tuple(int(x) for x in j if x != 'x') for j in text]
    return text


def fold_text(text1, text2):
    x = [0] * (max(text1[0][1], text2[0][1] + 1))
    for i in text1 + text2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key=lambda r: r[1], reverse=True)
    return res


def get_sum(text: object) -> object:
    var = ['*x^'] * len(text)
    coefs = [x[0] for x in text]
    degrees = [x[1] for x in text]
    new_text = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_text:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_text = list(itertools.chain(*new_text))
    new_text[-1] = ' = 0'
    return "".join(map(str, new_text))


def write_to_file(file, text):
    with open(file, 'w') as data:
        data.write(text)


text1 = read_file(file1)
text2 = read_file(file2)
text1_1 = convert_file(text1)
text1_2 = convert_file(text2)
text123 = fold_text(text1_1, text1_2)
text_sum = get_sum(fold_text(text1_1, text1_2))
write_to_file(file_sum, text_sum)

print(text1)
print(text2)
print()
print(text1_1)
print(text1_2)
print()
print(text123)
print()
print(text_sum)