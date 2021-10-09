# Второе задание

message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(message_list):
    if message_list[i].isdigit() or message_list[i][1:].isdigit():
        message_list[i] = message_list[i].zfill(2)
        message_list.insert(i + 1, ' "')
        message_list.insert(i, '" ')
        i += 1
        message_list[i] = message_list[i].replace('+5', '+05', 1)
    i += 1
message_list = ' '.join(message_list)
print(message_list.replace('  ', ''))