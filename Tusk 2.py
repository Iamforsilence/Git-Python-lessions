# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Можно ли в одном блоке with вводить несколько запросов? Т.е. если обьединить
# with open("text_file_2.txt", encoding="UTF-8") as text_file:
# print(len(text_file.readlines()))
#     for line in text_file:
#         print(len(line.split()))
# то код не работает корректно. Или для этого нужно без менеджера писать, через open\close?

with open("text_file_2.txt", encoding="UTF-8") as text_file:
    for line in text_file:
        print(len(line.split()))

with open("text_file_2.txt", encoding="UTF-8") as text_file:
    print(len(text_file.readlines()))
