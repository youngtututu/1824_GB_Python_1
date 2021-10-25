# Третье задание
import sys

users = {}
usr = []
hobby = []
with open('users.csv', 'r', encoding='utf-8') as f:
    for row_1 in f:
        usr.append(row_1[:-1])
with open('hobby.csv', 'r', encoding='utf-8') as f_2:
    for row_2 in f_2:
        hobby.append(row_2[:-1])
if len(usr) < len(hobby):
    sys.exit(1)
for i in range(len(usr)):
    users[usr[i]] = hobby[i]
f = open('result.csv', 'w')
f.write(str(users))






