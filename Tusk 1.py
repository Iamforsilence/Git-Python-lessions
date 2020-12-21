# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


text_file = open("text_file_1.txt", "w")
line = "Данные"
while True:
    if line == "":
        break
    else:
        line = input("Введите данные:")
        text_file.write(line + "\n")

text_file.close()
