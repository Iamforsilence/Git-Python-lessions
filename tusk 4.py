# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

with open("text_file_4.txt", encoding="UTF-8") as text_file:
    content = text_file.readline().split()
    content[0] = "Один"
    first_str = " ".join(content)
    with open("new_file_tusk_4.txt", "w") as new_file:
        print(first_str, file=new_file)

    content = text_file.readline().split()
    content[0] = "Два"
    second_str = " ".join(content)
    with open("new_file_tusk_4.txt", "a") as new_file:
        print(second_str, file=new_file)

    content = text_file.readline().split()
    content[0] = "Три"
    thirst_str = " ".join(content)
    with open("new_file_tusk_4.txt", "a") as new_file:
        print(thirst_str, file=new_file)

    content = text_file.readline().split()
    content[0] = "Четыре"
    fourth_str = " ".join(content)
    with open("new_file_tusk_4.txt", "a") as new_file:
        print(fourth_str, file=new_file)
