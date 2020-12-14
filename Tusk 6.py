# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв
# в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

import re


def int_func(text):
    text = text.capitalize()
    return text


while True:
    word_person = input("Введите слово из маленьких латинских букв:")
    word_list = input("Введите слова, состоящие из маленьких латинских букв, через пробел:")
    if re.search(r'[аЯ-яА]', word_person) or re.search(r'[аЯ-яА]', word_list):
        print("Вы ввели некорректный символ. Вводите только латинские буквы.")
    else:
        break
print(int_func(word_person))

word_list = word_list.split()
new_list = []
for i in word_list:
    int_func(i)
    new_list.append(int_func(i))
print(new_list)
