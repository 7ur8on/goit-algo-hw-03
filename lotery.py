import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1): #  обмеження для параметрів
        my_list = list() # створюємо пустий список
        return list(my_list)  # повертаємо пустий список
    sample_numbers = sorted(random.sample(range(min, max + 1), quantity)) # створюємо список з унікальними значеннями
    return sample_numbers    # повертаємо і перетворюємо у список
print(get_numbers_ticket(1, 1000, 5))   # викликаємо функцію з параметрами
print(get_numbers_ticket(0, 50, 5))  # має вивести пустий список
print(get_numbers_ticket(1, 1001, 10))  # має вивести пустий список
print(get_numbers_ticket(50, 50, 5))  # має вивести пустий список
print(get_numbers_ticket(1, 50, 0))  # має вивести пустий список
print(get_numbers_ticket(1, 50, 51))  # має вивести пустий список
print(get_numbers_ticket(10, 20, 15))  # має вивести пустий список
print(get_numbers_ticket(1, 10, 6))  # повертає відсортований список унікальних значень