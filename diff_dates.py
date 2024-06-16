from datetime import datetime

random_date = "2024-06-10"

def get_days_from_today(date):
    return (datetime.now() - datetime.strptime(date, "%Y-%m-%d")).days

print(get_days_from_today(random_date))