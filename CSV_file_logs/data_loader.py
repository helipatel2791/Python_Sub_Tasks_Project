from dbconnection import getcursorconnection
import os
import glob
import csv
import shutil
import time

def loadfiletodb():
    conn, cursor = getcursorconnection()
    list_of_files = glob.glob('C:/Users/helip/PycharmProjects/CSV_file_logs/data/incoming/*.csv')
    latest_file_path = max(list_of_files, key=os.path.getctime)
    latest_file = os.path.basename(latest_file_path)
    print(latest_file)

    # update file name and status to database
    sql_query_1 = "INSERT INTO files(file_name, process_status) VALUES(%s,%s)"
    cursor.execute(sql_query_1, (latest_file, 'In-Progress'))
    conn.commit()

    file_data = []
    with open(latest_file_path, mode='r') as r:

        # get row_count of current file
        file_reader = csv.reader(r)
        row_count = sum(1 for row in file_reader) - 1
        print(row_count)

        r.seek(0)

        # read file data
        for f in file_reader:
            print(f)
            file_data.append(f)

    # remove header before inserting records to database
    file_data = file_data[1:]
    print(file_data)

    sql_query_2 = "SELECT file_id FROM files WHERE file_name = %s"
    cursor.execute(sql_query_2, latest_file)
    current_file_id = cursor.fetchone()[0]
    print(current_file_id)

    # insert file records to database
    sql_query_3 = "INSERT INTO files_data(file_name_id, id, age, sex, country, date_confirmation, recovered) VALUES(%s,%s,%s,%s,%s,%s,%s);"
    for row in file_data:
        try:
            cursor.execute(sql_query_3, (current_file_id, row[0], row[1], row[2], row[3], row[4], row[5]))
            conn.commit()

        except Exception:
            pass

    # get rowcount of SQL table of file_id that has been recently uploaded
    sql_query_4 = "SELECT COUNT(*) FROM files_data WHERE file_name_id = %s;"
    cursor.execute(sql_query_4, current_file_id)
    table_row_count = cursor.fetchone()[0]
    print(table_row_count)

    # if all data from file uploaded in MYSQL table then update status to success and move file to success folder
    if table_row_count == row_count:
        sql_query_5 = "UPDATE files SET process_status = 'Success', num_rows = %s WHERE file_id = %s;"
        cursor.execute(sql_query_5, (table_row_count, current_file_id))
        conn.commit()
        shutil.move(latest_file_path, 'C:/Users/helip/PycharmProjects/CSV_file_logs/data/processed/success')
    else:
        sql_query_5 = "UPDATE files SET process_status = 'Failed' WHERE file_id = %s;"
        cursor.execute(sql_query_5, current_file_id)
        conn.commit()
        shutil.move(latest_file_path, 'C:/Users/helip/PycharmProjects/CSV_file_logs/data/processed/failed')



    cursor.close()
    conn.close()



if __name__ == '__main__':
    while True:
        loadfiletodb()
        time.sleep(6*60)

