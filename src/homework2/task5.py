""" Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.

"""


INPUT_LIST = input('Пожалуйста, введите, список разделяя элементы пробелом: ').split()

ANSWER = []
for i in INPUT_LIST:
    if INPUT_LIST.count(i) == 1:
        ANSWER.append(i)
print('Уникальные элементы в списке:', ANSWER)
