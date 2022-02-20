""" Все подсписки заданного списка
Используя определение подсписка из задачи №8, напишите программу, возвращающую список,
содержащий все возможные подсписки заданного.
Например, в число подсписков списка [1, 2, 3] входят следую-щие: [], [1], [2], [3], [1, 2],
[2, 3] и [1, 2, 3]. Заметьте, что ваша программа должна вернуть как минимум один пустой список,
гарантированно являющийся подсписком для любого списка.

"""


LIST = input('Пожалуйста, введите список, разделяя элементы пробелом:').split()
n = len(LIST)
SUBLIST = [[]]
SUBLIST += [LIST[i:j] for i in range(n + 1) for j in range(i + 1, n + 1)]
print('Возможными подсписками введенного списка являются:\n', SUBLIST)
