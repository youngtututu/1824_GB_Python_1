# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(item_dict):
    for en_num, ru_num in num_dict.items():
        if en_num == item_dict:
            return 'Перевод на русский: ' + ru_num

num_dict = {
    'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

item_dict = input('Введите число от 0 до 10 на английском языке: ')
print(num_translate(item_dict))