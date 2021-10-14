# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
#
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [57.8, 46.51, 97, 6.05, 77, 5.54, 5, 10.20, 45.05]

price_list_2 = []
for i in range(len(price_list)):
    rub = int(price_list[i])
    kop = int((price_list[i]*100) % 100)
    result = (f'{rub:02} руб {kop:02} коп')
    price_list_2.append(result)
print(price_list_2)

print(id(price_list))
price_list.sort()
print(price_list)
print(id(price_list))

price_list_2 = price_list.copy()
price_list_2.reverse()
print(price_list_2)

price_list_3 = []
for i in range(len(price_list)):
    rub = int(price_list[i])
    kop = int((price_list[i]*100) % 100)
    result = (f'{rub:02} руб {kop:02} коп')
    price_list_3.append(result)
print(price_list_3[-5:])