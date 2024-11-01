def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {incorrect_data}')
    c = (result,incorrect_data)
    return c

def calculate_average(numbers):
    try:
        c = personal_sum(numbers)
        return c[0] / (len(numbers) - c[1])
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')