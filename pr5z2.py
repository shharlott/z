# Ввод начальной дистанции от пользователя
distance = float(input("Введите дистанцию, которую спортсмен пробежал в 1-ый день (в км): "))

# Инициализация переменных
day = 1  # Номер текущего дня
total_distance = distance  # Общий пройденный путь

# Цикл с условием для подсчета пройденного пути за неделю
while day < 8:
    print(f"День {day}: {distance:.2f} км")

    # Увеличение дистанции на 10% и обновление общего пути
    distance *= 1.1
    total_distance += distance

    day += 1

# Вывод общего пройденного пути за неделю
print(f"Суммарный путь спортсмена за 1 неделю: {total_distance:.2f} км")
