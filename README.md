# python-up-excel-to-mysql

1. Buat database dengan nama "db_simonkelor"
2. Buat tabel monitoring_realtimes dengan isi kolom (id(key), parameter(text), value(doubel), date(timestamp))
3. install python bagi yang belum install
4. install beberapa library yang digunakan

    - pip install mysql-connector-python
    - pip install pandas
    - pip install time
    
5. Ubah directory file terlebih dahulu pada function tambah_data dan update_data sesuaikan dengan directory file excel yang Anda gunakan

    dataset = pd.read_excel('D:\Documents\monitoring_realtime.xlsx')
    
6. lakukan save file 
7. jalankan file
