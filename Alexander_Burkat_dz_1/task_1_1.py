# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = 400153

secs = duration % 60
mins = duration // 60 % 60
hours = duration // 60 ** 2 % 24
days = duration // 60 ** 2 // 24

if duration < 60:
    print(duration, 'сек')
elif days:
    print(days, 'дн', hours, 'час', mins, 'мин', secs, 'сек')  # 4 дн 15 час 9 мин 13 сек
elif hours:
    print(hours, 'час', mins, 'мин', secs, 'сек')
else:
    print(mins, 'мин', secs, 'сек')
