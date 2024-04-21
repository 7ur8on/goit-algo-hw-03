import random
my_list = set() # створюємо пусту множину
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max: #  обмеження для параметрів
        return list(my_list)  # повертаємо пустий список
    while len(my_list) < quantity:  # запускаєм цикл до певного параметру
        random_number = random.randint(min, max)    # генеруєм випадкове число
        my_list.add(random_number)   # як-що число не повторюється то додаєм в множину
    return list(my_list)    # повертаємо і перетворюємо у список
print(get_numbers_ticket(1, 1000, 5))   # викликаємо функцію з параметрами