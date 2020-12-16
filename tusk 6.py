# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count, cycle

iterator1 = count(1)
for i in iterator1:
    if i > 10:
        break
    print(i, end=" ")

lst = ["a", "b", "c", ]
iterator2 = cycle(lst)
step = 0
for el in iterator2:
    step += 1
    if step == 10:
        break
    print(el, end=", ")

