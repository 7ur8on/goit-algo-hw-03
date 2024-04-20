from datetime import datetime

random_date = "2020-10-09"      # випадкова дата
def get_days_from_today(date):
    date_format = datetime.strptime(date, "%Y-%m-%d")   # задаєм формат дати
    current_date = datetime.now()   # поточна дата
    difference = current_date - date_format    # різниця між датами
    return difference.days      # повертаєм різницю у днях
print(get_days_from_today(random_date))     # викликаєм функцію і надруковуєм результат функції