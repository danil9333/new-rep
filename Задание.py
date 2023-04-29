money = int(input("Введите желаемую сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L = list(per_cent.values())

L1 = (list(map(lambda x: money*x/100, L)))
print ([int(x) for x in L1])
print ("Максимальная сумма, которую вы можете заработать:", max(L1)