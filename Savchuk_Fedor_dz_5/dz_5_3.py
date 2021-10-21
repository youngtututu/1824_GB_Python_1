# Третье задание

tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
dict_1 = tuple(zip(tutors, klasses))
dict_2 = list(dict_1)
print(dict_2)
dict_gen = (dict_2[i] for i in range(len(dict_1)))

while True:
    try:
        print(type(dict_gen), '-', next(dict_gen))
    except StopIteration:
        break
