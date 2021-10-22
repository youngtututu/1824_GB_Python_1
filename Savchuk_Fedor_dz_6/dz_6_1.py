import re

users_list = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        string_logs = re.split('--|"| ', row)
        user_list = string_logs[0], string_logs[6], string_logs[7]
        users_list.append(user_list)

print(*users_list, sep='\n')
print(type(users_list))