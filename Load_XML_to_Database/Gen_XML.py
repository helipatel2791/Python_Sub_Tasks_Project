import xml.etree.ElementTree as ET
import csv


def generate_xml(file_name):
    # read CSV file in list of lists
    file_data = []
    with open(file_name, mode='r') as r:
        file_reader = csv.reader(r)
        for row in file_reader:
            file_data.append(row)

    # remove header
    file_data = file_data[1:]

    root = ET.Element("USA_Cars")
    for record in file_data:
        try:
            c1 = ET.Element("USA_Car")
            root.append(c1)
            id = ET.SubElement(c1, 'ID')
            price = ET.SubElement(c1, 'price')
            brand = ET.SubElement(c1, 'brand')
            model = ET.SubElement(c1, 'model')
            year = ET.SubElement(c1, 'year')
            title_status = ET.SubElement(c1, 'title_status')
            mileage = ET.SubElement(c1, 'mileage')
            color = ET.SubElement(c1, 'color')
            state = ET.SubElement(c1, 'state')
            country = ET.SubElement(c1, 'country')
            condition = ET.SubElement(c1, 'condition')

            id.text = record[0]
            price.text = record[1]
            brand.text = record[2]
            model.text = record[3]
            year.text = record[4]
            title_status.text = record[5]
            mileage.text = record[6]
            color.text = record[7]
            state.text = record[8]
            country.text = record[9]
            condition.text = record[10]

        except:
            pass
    et = ET.tostring(root, encoding='unicode')
    print(type(et))
    with open('USA_cars_dataset.xml', 'w') as open_file:
        open_file.write(et)



generate_xml('C:/Users/helip/PycharmProjects/Load_XML_to_Database/USA_cars_datasets.csv')