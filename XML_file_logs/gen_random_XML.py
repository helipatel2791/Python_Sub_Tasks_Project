import random
import datetime
import os
import string
import xml.etree.ElementTree as ET


def random_string(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def get_random_date():
    start_date = datetime.date(2020,1,1)
    end_date = datetime.date(2020,6,30)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    print (datetime.timedelta(days=random_number_of_days))
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def create_xml(path, filename):
    filedatetime = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    name = filename + filedatetime + '.xml'
    completeName = os.path.join(path, name)
    if not os.path.exists(path):
        os.makedirs(path)

    root = ET.Element("Employee_Data")
    for i in range(10):
        employee = ET.SubElement(root, "employee", attrib={'id': str(i)})
        name = ET.SubElement(employee, "name" )
        age = ET.SubElement(employee, "age")
        sex = ET.SubElement(employee, "sex")
        country = ET.SubElement(employee, "country")
        date_joined = ET.SubElement(employee, "date_joined")
        points = ET.SubElement(employee, "points")

        name.text = random_string(random.randint(5,15)) # generate random names of length between 5 and 15
        age.text = str(random.randint(21,60))
        sex.text = random.choice(['male','female', 'other'])
        country.text = random.choice(['india', 'USA', 'canada', 'australia', 'UAE'])
        date_joined.text = str(get_random_date())
        points.text = str(round(random.uniform(10, 100), 2))

    tree = ET.ElementTree(root)
    tree.write(completeName)


create_xml('C:/Users/helip/PycharmProjects/XML_file_logs/incoming', 'employee_data_')

