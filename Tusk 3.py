# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
# фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


# Код работает, но мне кажется, что как то криво написано, или я не прав?

with open("text_file_3.txt", encoding="UTF-8") as text_file:
    for price in text_file:
        price = price.split()
        price[1] = int(price[1])
        if price[1] < 20000:
            print(price[0])

summa = 0
text_file = open("text_file_3.txt", encoding="Utf-8")
for line in text_file:
    content = line.split()
    content[1] = int(content[1])
    summa = (summa + content[1])
average = summa / 3
print(average)
text_file.close()
