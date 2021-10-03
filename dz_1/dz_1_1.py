# Задание первое
# Никогда не программировал, поэтому было сложно сделать даже его
# Наверное тут есть еще проще варианты решения

duration = int(input("Введите количество секунд: "))
days = duration // 86400
hours = (duration - (days * 86400)) // 3600
minutes = (duration - ((days * 86400) + (hours * 3600))) // 60
seconds = duration - ((days * 86400) + (hours * 3600) + (minutes * 60))
# print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
if days > 0:
    print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
elif hours > 0:
    print(hours, "час", minutes, "мин", seconds, "сек")
elif minutes > 0:
    print(minutes, "мин", seconds, "сек")
else:
    print(seconds, "сек")