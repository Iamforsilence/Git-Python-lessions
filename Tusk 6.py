# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


lst_quantity_things = []
with open("text_file_6.txt", encoding="UTF-8") as text_file:
    line_1 = text_file.readline()
    line_2 = text_file.readline()
    line_3 = text_file.readline()


# Так как числа в текстовом файле были не разделены пробелом,решил вычленить их через цикл. Сделал функцию,
# которая принимает строку из файла, вычленяет цифры и закидывает их в список. И функцию для подсчета суммы
# элементов списка. А дальше наполнял пустой словарь. Были бы пробелы между числами и сокращениями, было бы полегче:)
# Если можно, напишите, как можно было бы это сделать проще с точки зрения длинны кода?:)

def number_lst(line):
    length_line = len(line)
    i = 0
    while i < length_line:
        number = ""
        x = line[i]
        while "0" <= x <= "9":
            number += x
            i += 1
            if i < length_line:
                x = line[i]
            else:
                break
        i += 1
        if number != "":
            lst_quantity_things.append(int(number))


def sum_lst(lst):
    sum_el = 0
    for i in lst:
        sum_el = sum_el + i
    return sum_el


final_dict = {}

line_new = line_1.split()
number_lst(line_1)
final_dict[line_new[0]] = sum_lst(lst_quantity_things)
lst_quantity_things.clear()

line_new = line_2.split()
number_lst(line_2)
final_dict[line_new[0]] = sum_lst(lst_quantity_things)
lst_quantity_things.clear()

line_new = line_3.split()
number_lst(line_3)
final_dict[line_new[0]] = sum_lst(lst_quantity_things)
print(final_dict)
