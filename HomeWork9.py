import random

date_month = [1, 2, 3,
              4, 5, 6,
              7, 8, 9,
              10, 11, 12,
              13, 14, 15,
              16, 17, 18,
              19, 20, 21,
              22, 23, 24,
              25, 26, 27,
              28, 29, 30]
weather = ['Sunny', 'Rainy', 'Storm',
           'Thunder', 'Snow', 'Snowfall',
           'Cloudy', 'Hail', 'Eclipse']


def print_params(date_month, weather):
    day = random.choice(date_month)
    weather_day = random.choice(weather)
    print(date_month)
    print(weather)
    return day, weather_day


print_params(date_month, weather)
print_params(date_month, weather)
