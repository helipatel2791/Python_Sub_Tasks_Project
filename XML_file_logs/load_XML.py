import xml.etree.ElementTree as ET
from dbconnection import getcursorconnection
import glob
import os
import shutil

def load_xml_to_table():
    # get PYMYSQL cursor and conn element
    conn, cursor = getcursorconnection()

    # get file_name from incoming folder
    file_path = glob.glob('C:/Users/helip/PycharmProjects/XML_file_logs/incoming/*.xml')[0]
    file = os.path.basename(file_path)
    print(file)

    sql_query_1 = "INSERT INTO files(file_name, process_status) VALUES(%s,%s)"
    cursor.execute(sql_query_1, (file, 'In-Progress'))
    conn.commit()

    # parse an xml file
    tree = ET.parse(file_path)
    print(tree)
    root = tree.getroot()
    print(root)
    # use below two lists if you want lists column wise
    '''
    employee_id = [i for i in range(len(root.findall('employee')))]
    employee_list = [[t.text for t in root.iter(tag)] for tag in
                     ['name', 'age', 'sex', 'country', 'date_joined', 'points']]
    '''
    # get list row by row from xml
    tags = ['name', 'age', 'sex', 'country', 'date_joined', 'points']
    employee_list = []
    for y in root.iter('employee'):
        one_employee_list = []
        one_employee_list.append(str(y.attrib['id']))
        for tag in tags:
            for t in y.iter(tag):
                one_employee_list.append(t.text)
        employee_list.append(one_employee_list)
    print(employee_list)

    # get id of current file to be added to employee table
    sql_query_2 = "SELECT file_id FROM files WHERE file_name = %s"
    cursor.execute(sql_query_2, file)
    current_file_id = cursor.fetchone()[0]
    print(current_file_id)

    # Now, insert employee_list to employee table along with file id
    sql_query_3 = "INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    for record in employee_list:
        cursor.execute(sql_query_3, (str(current_file_id), record[0],record[1],record[2],record[3],record[4],record[5],record[6]))
        conn.commit()

    # get rowcount of MYSQL employee table with recent uploaded data
    sql_query_4 = "SELECT COUNT(*) FROM employee WHERE file_id = %s;"
    cursor.execute(sql_query_4, current_file_id)
    table_row_count = cursor.fetchone()[0]
    print(table_row_count)

    # if all data from xml file uploaded in MYSQL table then update status to success and move file to success folder
    if table_row_count == len(root.findall('employee')):
        sql_query_5 = "UPDATE files SET process_status = 'success', num_rows = %s WHERE file_id = %s;"
        cursor.execute(sql_query_5, (table_row_count, current_file_id))
        conn.commit()
        shutil.move(file_path, 'C:/Users/helip/PycharmProjects/XML_file_logs/processed/success')
    else:
        sql_query_5 = "UPDATE files SET process_status = 'failed' WHERE file_id = %s;"
        cursor.execute(sql_query_5, current_file_id)
        conn.commit()
        shutil.move(file_path, 'C:/Users/helip/PycharmProjects/XML_file_logs/processed/failed')

    cursor.close()
    conn.close()

load_xml_to_table()
