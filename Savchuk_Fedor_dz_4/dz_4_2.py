from utils import currency_rates

# Список для проверки многократного вывода
cur_list = ['USD', 'EUR']

# Реализация многократного запроса к функции
for i in cur_list:
    answer = currency_rates(i)
    print(f'{i} {answer}')