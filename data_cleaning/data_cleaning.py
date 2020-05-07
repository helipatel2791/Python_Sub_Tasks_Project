from dbconnection import getcursorconnection
import os
import glob
import csv
import  time

def loadfiletodb():
    conn, cursor = getcursorconnection()
    list_of_files = glob.glob('C:/Users/helip/PycharmProjects/data_cleaning/source_file/*.csv')
    latest_file_path = max(list_of_files, key=os.path.getctime)
    latest_file = os.path.basename(latest_file_path)
    print(latest_file)

    file_data = []
    with open(latest_file_path, mode='r') as r:
        file_reader = csv.reader(r)

        # read file data
        for f in file_reader:
            print(f)
            file_data.append(f)

    # remove header before inserting records to database
    file_data = file_data[1:]
    print(file_data)

    # insert file records to database
    bad_data_path = 'C:/Users/helip/PycharmProjects/data_cleaning/bad_data_file/'
    valid_data_path = 'C:/Users/helip/PycharmProjects/data_cleaning/valid_data_file/'
    sql_query_3 = "INSERT INTO files_data(id, age, sex, country, date_confirmation, recovered) VALUES(%s,%s,%s,%s,%s,%s);"
    for row in file_data:
        try:
            cursor.execute(sql_query_3, (row[0], row[1], row[2], row[3], row[4], row[5]))
            conn.commit()
            with open(valid_data_path + 'valid_' + latest_file, 'a', newline='') as open_file:
                csv_writer = csv.writer(open_file, delimiter=',')
                csv_writer.writerow(row)

        except:
            with open(bad_data_path + 'bad_' + latest_file, 'a', newline='') as open_file:
                csv_writer = csv.writer(open_file, delimiter=',')
                csv_writer.writerow(row)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    while True:
        loadfiletodb()
        time.sleep(6*60)

