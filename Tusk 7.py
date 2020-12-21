# 7. Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).

import json

with open("text_file_7.txt", encoding="UTF-8") as text_file:
    content_firm_1 = text_file.readline().split()
    content_firm_2 = text_file.readline().split()
    content_firm_3 = text_file.readline().split()

profit_firm_1 = int(content_firm_1[2]) - int(content_firm_1[-1])
profit_firm_2 = int(content_firm_2[2]) - int(content_firm_2[-1])
profit_firm_3 = int(content_firm_3[2]) - int(content_firm_3[-1])
average_proceeds = (profit_firm_1 + profit_firm_2 + profit_firm_3) / 3

my_list = [{content_firm_1[0]: profit_firm_1, content_firm_2[0]: profit_firm_2, content_firm_3[0]: profit_firm_3},
           {'average_profit': average_proceeds}]

print(my_list)

with open("text_file_7.json", "w") as new_json:
    json.dump(my_list, new_json)
