# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("text_file_5.txt", "w") as text_file:
    text_file.write("1 2 3 4 5")

with open("text_file_5.txt", encoding="UTF-8") as text_file:
    content = text_file.readline().split()
    sum_i = 0
    for i in content:
        i = int(i)
        sum_i = i + sum_i
print(sum_i)
