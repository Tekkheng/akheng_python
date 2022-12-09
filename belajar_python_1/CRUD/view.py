# from .cek_db import DB_NAME
from .operasi import read,create_first_data,update
import os
import CRUD

def read_data(**kwargs):
    try:
        data = read()
        print(f"| {'No'} | {'PK':^4} | {'Nim':^15} | {'Nama':^30} | {'Fakultas':^30} | {'Tanggal Lahir':^10} | {'Created at':^10} |")
        for no,i in enumerate(data):
            data_break = i.split(",")
            pk = data_break[0]
            nim = data_break[1]
            nama = data_break[2]
            fakultas = data_break[3]
            tgl_lhr = data_break[4]
            created_at = data_break[5][:-1]
            
            print(f"| {no+1:^2} | {pk:^4} | {nim:^15} | {nama:.30} | {fakultas:.30} | {tgl_lhr:^13} | {created_at:^10} |")
        
        if not "edit" in kwargs:
            b = input("\nKembali ke menu? Enter: ")
        
    except:
        print("Gagal Read Data")

def create_data():
    try :
        with open(f"CRUD/{CRUD.DB_NAME}","a",encoding="utf-8") as file:
            dt = create_first_data()
            file.write(dt)
    except:
        print("Gagal create data!")

def update_data():
    try:
        with open(f"CRUD/{CRUD.DB_NAME}","r+",encoding="utf-8") as file:
            data = read()
            p_dt = len(data)
            while True:
                sistem_operasi = os.name
                match sistem_operasi:
                    case "posix" : os.system("clear")
                    case "nt" : os.system("cls")

                print("Update Dengan Nomor Data".center(130,"-"))
                read_data(edit = p_dt)
                try:
                    no_index = int(input("\nMasukkan Nomor data yang mau di edit : "))
                except:
                    print("nomor index harus angka!")
                    continue
                data_edit = data[no_index-1]
                hasil = update(no_index-1,p_dt,data_edit)

                tampung = CRUD.TEMPLATE.copy()
                tampung.update({
                        "pk" : hasil[0],
                        "nim" : hasil[1],
                        "nama" : hasil[2] + CRUD.TEMPLATE["nama"],
                        "fakultas" : hasil[3] + CRUD.TEMPLATE["fakultas"],
                        "tgl_lhr" : hasil[4],
                        "created_at" : hasil[5]
                })
                result = "{},{},{},{},{},{}\n".format(tampung["pk"],tampung["nim"],tampung["nama"],tampung["fakultas"],tampung["tgl_lhr"],tampung["created_at"])
                try:
                    data[no_index-1] = result
                    file.write(data)
                    print(data) 
                    s=input("s :")
                    print("Data berhasil Di update")
                except:
                    print("Proses Update Gagal")
    except:
        print("Gagal Update, data masih kosong,silahkan membuat data dulu!")