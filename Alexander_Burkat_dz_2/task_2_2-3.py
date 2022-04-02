weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
msg = ''

while i < len(weather):
    if weather[i].lstrip('+-').isdigit():
        if weather[i].startswith('+') or weather[i].startswith('-'):
            weather[i] = f'{weather[i][0]}{int(weather[i]):02d}'
        else:
            weather[i] = f'{int(weather[i]):02d}'
        weather.insert(i, '"')
        weather.insert(i + 2, '"')
        msg += ''.join(weather[i:i + 2])
        i += 2
    else:
        msg += weather[i] + ' '
        i += 1

print(weather)
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
print(msg)
# в "05" часов "17" минут температура воздуха была "+05" градусов

