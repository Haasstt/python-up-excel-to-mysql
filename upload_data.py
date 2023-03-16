import mysql.connector
import pandas as pd
import time

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_simonkelor"
)

if(connection):
    print("connection success")
else:
    print("gagal connection")


def tambah_data_mahasiswa(connection):
    dataset = pd.read_excel('D:\Documents\monitoring_realtime.xlsx')
    for i in dataset.index:    
        parameter = dataset['Parameter'][i]
        value = dataset['Value'][i]

        if(value == '-'):
            value = 0
            cursor = connection.cursor()
            sql = "INSERT INTO monitoring_realtimes VALUES(NULL, %s, %s, NULL)"
            cursor.execute(sql, (parameter, value))
            connection.commit()
            print("{} data berhasil disimpan".format(cursor.rowcount))
        else:
            cursor = connection.cursor()
            sql = "INSERT INTO monitoring_realtimes VALUES(NULL, %s, %s, NULL)"
            cursor.execute(sql, (parameter, value))
            connection.commit()
            print("{} data berhasil disimpan".format(cursor.rowcount))

def update_data(connection):
    dataset = pd.read_excel('D:\Documents\monitoring_realtime.xlsx')

    for i in dataset.index:    
        parameter = dataset['Parameter'][i]
        value = dataset['Value'][i]

        if(value == '-'):
            value = 0
            cursor = connection.cursor()
            sql = "UPDATE monitoring_realtimes SET value=%s WHERE parameter=%s"
            cursor.execute(sql, (value, parameter))
            connection.commit()
        else:
            cursor = connection.cursor()
            sql = "UPDATE monitoring_realtimes SET value=%s WHERE parameter=%s"
            cursor.execute(sql, (value, parameter))
            connection.commit()


tambah_data_mahasiswa(connection)

i = 0
x = 0

while i <= x:
    total_second = 1

    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
        
    update_data(connection)
    print("data berhasil diupdate")
    x = x+1
