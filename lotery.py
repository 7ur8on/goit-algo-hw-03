import random
my_list = set() # створюємо пусту множину
def get_numbers_ticket(min, max, quantity):
    while len(my_list) < quantity:  # запускаєм цикл до певного параметру
        random_number = random.randint(min, max)    # генеруєм випадкове число
        my_list.add(random_number)   # як-що число не повторюється то додаєм в множину
    return list(my_list)    # повертаємо і перетворюємо у список
print(get_numbers_ticket(1, 10, 5))   # викликаємо функцію з параметрами