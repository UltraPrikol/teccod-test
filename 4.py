def sort_by_length(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings


def sort_by_length_reverse(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(strings[j]) < len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings


strings_list = ['Яблоко', 'Банан', 'Помидор', 'Пекинская капуста', 'Лук', 'Арбуз']

sorted_strings_asc = sort_by_length(strings_list)[:]
sorted_strings_desc = sort_by_length_reverse(strings_list)

print('Сортировка по длине в порядке возрастания: {}'.format(sorted_strings_asc))
print('Сортировка по длине в порядке убывания: {}'.format(sorted_strings_desc))
