weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for el in weather:
    if el.lstrip('+-').isdigit() and weather[weather.index(el) - 1] != '"' and weather[weather.index(el) + 1] != '"':
        weather.insert(weather.index(el) + 1, '"')
        weather.insert(weather.index(el), '"')
        if el.startswith('+') or el.startswith('-'):
            weather[weather.index(el)] = f'{el[0]}{int(weather[weather.index(el)]):02d}'
        else:
            weather[weather.index(el)] = f'{int(weather[weather.index(el)]):02d}'
    elif weather[weather.index(el)] == '"' and weather[weather.index(el) - 1] != ' ':  # and weather[weather.index(el) + 1] != ' ':
        weather.insert(weather.index(el), ' ')

print(weather)
print(''.join(weather))

