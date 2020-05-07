import csv
import random
import datetime
import time
import os
import string

def get_random_date():
    start_date = datetime.date(2020,1,1)
    end_date = datetime.date(2020,6,30)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    print (datetime.timedelta(days=random_number_of_days))
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def create_csv(path, filename):
    filedatetime = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    name = filename + filedatetime + '.csv'
    completeName = os.path.join(path, name)
    if not os.path.exists(path):
        os.makedirs(path)
    countries = ['china', 'india', 'USA', 'itly', 'spain', 'canada']
    with open(completeName, mode='w', newline='') as open_file:
        csv_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(['ID', 'age', 'sex', 'country', 'date_confirmation', 'recovered'])
        for i in range(10):

            # generating bad rows to process data-cleansing later
            if i == random.randint(0, 10) and i == 2:
                letters = string.ascii_lowercase
                csv_writer.writerow((i + 1, random.randrange(1, 96), random.choice(['female', 'male', 'other']),
                                    ''.join(random.choice(letters) for l in range(10)),
                                     get_random_date(), random.choice(['yes', 'no'])))

            elif i == random.randint(0, 10) and i == 6:
                letters = string.ascii_lowercase
                csv_writer.writerow((i + 1, round(random.uniform(1, 100), 2), random.choice(['female', 'male', 'other']),
                                    random.choice(countries),get_random_date(), random.choice(['yes', 'no'])))

            elif i == random.randint(0, 10) and i == 9:
                letters = string.ascii_lowercase
                csv_writer.writerow((i + 1, round(random.uniform(0, 100), 2), random.choice(['female', 'male', 'other']),
                                    random.choice(countries),get_random_date()))

            # generating correct data to be loaded in MYSQL database
            else:
                csv_writer.writerow((i + 1, random.randrange(1, 96), random.choice(['female', 'male', 'other']),
                                    random.choice(countries), get_random_date(), random.choice(['yes', 'no'])))


if __name__ == '__main__':

    while True:
        create_csv('C:/Users/helip/PycharmProjects/data_cleaning/source_file', 'COVID_19_data_')
        time.sleep(5*60)
