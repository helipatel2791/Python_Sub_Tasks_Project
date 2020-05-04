from dbconnection import getcursorconnection
import xml.etree.ElementTree as ET
import pymysql

def loadxmltodb():
    # get cursor and coo object by function call
    conn, cursor = getcursorconnection()

    # parse an xml file
    tree = ET.parse('USA_cars_dataset.xml')
    print(tree)
    root = tree.getroot()
    print(len(root.findall('USA_Car')))
    print(root.tag)
    print(root[0].tag)

    # create an empty list to append with xml text
    usa_cars_list = []
    for y in range(len(root.findall('USA_Car'))):
        # an empty list for each row
        one_car_list = []
        for x in root[y]:
            print(x)
            one_car_list.append(x.text)
        # append usa_cars_list with one_car_list(one row), therefore usa_cars_list is now list of lists
        usa_cars_list.append(one_car_list)
    print(usa_cars_list)

    # save usa_cars_list to database
    for row in usa_cars_list:
        try:
            cursor.execute("INSERT INTO car VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            conn.commit()
        except:
            pass


    cursor.close()
    conn.close()


loadxmltodb()
