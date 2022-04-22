# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.

spam = {}

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        ip = line.split()[0]
        spam[ip] = 1 if ip not in spam else spam[ip] + 1


attacks = max(spam[ip] for ip in spam if spam[ip] > 1)

print(*filter(lambda tpl: tpl[1] == attacks, spam.items()))
