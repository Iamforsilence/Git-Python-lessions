# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv


def salary(output, rate, prize):
    output = int(output)
    rate = int(rate)
    prize = int(prize)
    result = (output * rate) + prize
    return result


print(salary(argv[1], argv[2], argv[3]))
