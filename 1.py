numbers = [1, 1, 2, 2, 3, 4]


def get_unique_number(num_list):
    unique_numbers = []

    for number in num_list:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


print(get_unique_number(numbers))
