# Задание второе
number_list = []
sum = 0
x = 0

for x in range (1, 1000, 2):
    x = x ** 3
    number_list.append(x)

x = 0

while x <= (len(number_list) - 1):
    divisibility_check = number_list[x]
    sum_this_digits = 0
    # while divisibility_check != 0:
    #     sum_this_digits += divisibility_check % 10
    #     divisibility_check = divisibility_check // 10
    # if sum_this_digits % 7 == 0:
    #     sum = sum + number_list[x]
    #     # print(cube_sum, cube_list[i], i, sum_this_digits)
    x += 1
    print(len(number_list))
# print(sum)




# a = input('Введите число: ')
#
# suma = 0
# mult = 1
#
# for digit in a:
#     suma += int(digit)
#     mult *= int(digit)
#
# print("Сумма:", suma)
# print("Произведение:", mult)
