# Задание второе
number_list = []
sum = 0
x = 0

for x in range(1, 1000, 2):
    x = x ** 3
    number_list.append(x)

x = 0

while x <= (len(number_list) - 1):
    check_index = number_list[x]
    sum_number= 0
    while check_index != 0:
        sum_number += check_index % 10
        check_index = check_index // 10
    if sum_number % 7 == 0:
        sum = sum + number_list[x]
    x += 1
print(sum)
