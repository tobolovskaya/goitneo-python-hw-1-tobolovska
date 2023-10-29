from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Поточний день
    today = datetime.today().date()

    # Структура для зберігання імен користувачів за днями тижня
    birthdays = defaultdict(list)

    # Перебираємо користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Перевірка, чи минув день народження цього року
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Різниця між днем народження та поточним днем
        delta_days = (birthday_this_year - today).days

        # Перевіряємо, чи день народження на наступний тиждень
        if 0 <= delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            # Якщо вихідний, переносимо на понеділок
            if day_of_week in [5, 6]:
                day_of_week = 0
            weekdays = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]

            birthdays[weekdays[day_of_week]].append(name)

    # Виводимо результат
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")


# Тестуємо функцію
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 10, 25)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 10, 21)},
]

get_birthdays_per_week(users)
