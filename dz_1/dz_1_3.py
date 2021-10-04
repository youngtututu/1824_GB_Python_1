# Задание третье
x = 1
last_number = 0

percent_list = [' процент', ' процента', ' процентов']
print(percent_list)

while x <= 100:
    last_number = x % 10
    if last_number == 1:
        print(x, percent_list[0])
    elif last_number in range(5, 10) or last_number == 0 or x in range(11, 15):
        print(x, percent_list[2])
    else:
        print(x, percent_list[1])
    x = x + 1