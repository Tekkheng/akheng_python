import random,string
import datetime as dt
import os
import CRUD

def random_str(p):
    r = "".join(random.choice(string.ascii_letters) for i in range(p))
    return r

def input_data():
    while True:
        pk = random_str(4)
        try : 
            while True:
                nim = int(input("Nim : "))
                s_nim = str(nim)
                if len(s_nim) > 0 and len(s_nim) < 15 and nim > 0:
                    nama = input("\nNama : ")
                    fakultas = input("Fakultas : ")
                    while True:
                        try:
                            tgl = int(input("Tanggal : "))
                            bulan = int(input("Bulan : "))
                            tahun = int(input("Tahun : "))
                            tgl_lhr = dt.datetime(tahun,bulan,tgl).strftime("%Y-%m-%d")
                            created_at = dt.datetime.now().strftime("%Y-%m-%d")
                            return pk,nim,nama,fakultas,tgl_lhr,created_at
                        except:
                            print("input harus angka dan format input harus benar!")
                else:
                    print("angka tidak boleh 0 atau minus, dan panjang angka maksimal 15 angka!")
                    continue
        except : 
            print("Nim harus angka!,silahkan input nim lagi!")

def create_first_data():
    tampung = CRUD.TEMPLATE.copy()
    hasil_input = input_data()
    
    tampung.update({
        "pk" : hasil_input[0],
        "nim" : hasil_input[1],
        "nama" : hasil_input[2] + CRUD.TEMPLATE["nama"],
        "fakultas" : hasil_input[3] + CRUD.TEMPLATE["fakultas"],
        "tgl_lhr" : hasil_input[4],
        "created_at" : hasil_input[5]
    })
    data = "{},{},{},{},{},{}\n".format(tampung["pk"],tampung["nim"],tampung["nama"],tampung["fakultas"],tampung["tgl_lhr"],tampung["created_at"])
    return data
    
def read():
    with open(f"CRUD/{CRUD.DB_NAME}","r") as file:
        data = file.readlines()
        return data
        
def update(*args):
    no_edit = args[0]
    p_dt = args[1]
    dt_edit = args[2]
    
    dt_edit_break = dt_edit.split(",")

    pk = dt_edit_break[0]
    nim = dt_edit_break[1]
    nama = dt_edit_break[2]
    fakultas = dt_edit_break[3]
    tgl_lhr = dt_edit_break[4]
    created_at = dt_edit_break[5][:-1]

    while True:
        sistem_operasi = os.name
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        dt_str = [f"Nim = {nim}",f"Nama = {nama}",f"Fakultas = {fakultas}",f"Tanggal Lahir = {tgl_lhr}","Exit"]
        print("Data Edit".center(40,"-"))
        for no,i in enumerate(dt_str):
            print(f"{no+1}.{i:.40}")
        print("")
        try:
            opsi = int(input("Masukkan nomor yg mau di edit: "))
            match opsi:
                case 1 : 
                    while True:
                        try:
                            nim = int(input("Nim : "))
                            s_nim = str(nim)
                            if len(s_nim) > 0 and len(s_nim) < 15 and nim > 0:
                                break
                            else:
                                print("Nim tidak boleh dibawah 0 dan batas lengthny 14")
                                continue
                        except:
                            print("Nim Harus Angka!")
                case 2 :
                    nama = input("Nama : ")
                case 3 :
                    fakultas = input("Fakultas : ")
                case 4 :
                    tgl = int(input("Tanggal : "))
                    bulan = int(input("Bulan : "))
                    tahun = int(input("Tahun : "))
                    tgl_lhr = dt.datetime(tahun,bulan,tgl).strftime("%Y-%m-%d")
                
                case 5:
                    return pk,nim,nama,fakultas,tgl_lhr,created_at 
        except:
            print("Harus angka!")

        
