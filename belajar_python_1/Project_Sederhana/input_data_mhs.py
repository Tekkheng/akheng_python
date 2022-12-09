#   KEYS NIM NAMA SKS BEASISWA tgl_Lahir Jurusan 

import datetime as dt
import os 
import string,random

def hapusDt(dSiswa):
    while True:
        keyny = input("masukkan key yg mau di Hapus : ")
        os.system("clear")
        print(f"KEY : {keyny}")
        print("")
        print("Hapus Data".center(20,"-"))
        
        dSiswa.pop(keyny)
        os.system("clear")
        tampilDt(dSiswa)
        lanjut = input("hapus lagi? y/n : ")
        
        if lanjut == "n":
            break
        elif lanjut == "y":
            continue
        else:
            print("pilihan tidak ada")
            continue

def editDt(dSiswa):
    keyny = input("masukkan key yg mau di edit : ")
    os.system("clear")
    print(f"KEY : {keyny}")
    print("")
    print("Edit Data".center(20,"-"))
    [nim,nm,sks,bsw,jrs,lhr]=inputData()
    dictSementara = {
        "nim":nim,
        "nama":nm,
        "sks":sks,
        "beasiswa":bsw,
        "jurusan":jrs,
        "lahir":lhr,
    }
    dSiswa.update({keyny:dictSementara})
    tampilDt(dSiswa)

def tampilDt(dSiswa):
    print("Tampil Data Siswa".center(77,"-"))
    print(f"|{'Key':^10}|{'Nim':^10}|{'Nama':^10}|{'Sks':^10}|{'Beasiswa':^10}|{'Jurusan':^10}|{'Lahir':^10}|")
    print("-"*77)
    for i in dSiswa.keys():
        nim_s = dSiswa[i]["nim"]
        nama_s = dSiswa[i]["nama"]
        sks_s = dSiswa[i]["sks"]
        beasiswa_s = dSiswa[i]["beasiswa"]
        jurusan_s = dSiswa[i]["jurusan"]
        lahir_s = dSiswa[i]["lahir"]
        
        print(f"|{i:^10}|{nim_s:^10}|{nama_s:^10}|{sks_s:^10}|{beasiswa_s:^10}|{jurusan_s:^10}|{lahir_s:^10}|\n")

def inputData():
    nim = int(input("Nim : "))
    nama = input("Nama : ")
    sks = int(input("Sks : "))
    beasiswa = input("ada/tidak: ")
    if beasiswa == "ada":
        beasiswa = True
    elif beasiswa == "tidak":
        beasiswa = False

    jurusan = input("Jurusan : ")

    tgl = int(input("Tanggal : "))
    bulan = int(input("Bulan : "))
    tahun = int(input("Tahun : "))
    
    lahir = dt.datetime(tahun,bulan,tgl).strftime("%x")
    print("-".center(20,"-"))
    print("")
    return nim,nama,sks,beasiswa,jurusan,lahir

def inputDt(dSiswa):
    structure_siswa = {
        "nim":"",
        "nama":"",
        "sks":"",
        "beasiswa":"",
        "jurusan":"",
        "lahir":"",
    }
    data_siswa={}

    while True:
        [nim,nm,sks,bsw,jrs,lhr]=inputData()

        dt_siswa = dict.fromkeys(structure_siswa.keys())

        dt_siswa.update({"nim":nim,"nama":nm,"sks":sks,"beasiswa":bsw,"jurusan":jrs,"lahir":lhr})

        keyny = "".join(random.choice(string.ascii_uppercase) for i in range(5))

        data_siswa.update({keyny : dt_siswa})
        dSiswa.update(data_siswa)

        print(f"|{'Key':^10}|{'Nim':^10}|{'Nama':^10}|{'Sks':^10}|{'Beasiswa':^10}|{'Jurusan':^10}|{'Lahir':^10}|")
        print("-"*77)
        for i in dSiswa.keys():
            nim_s = dSiswa[i]["nim"]
            nama_s = dSiswa[i]["nama"]
            sks_s = dSiswa[i]["sks"]
            beasiswa_s = dSiswa[i]["beasiswa"]
            jurusan_s = dSiswa[i]["jurusan"]
            lahir_s = dSiswa[i]["lahir"]

            print(f"|{i:^10}|{nim_s:^10}|{nama_s:^10}|{sks_s:^10}|{beasiswa_s:^10}|{jurusan_s:^10}|{lahir_s:^10}|")

            

        lanjut = input("\ninputlagi? y/n: ")
        print("")
        if lanjut == "n":
            return data_siswa
        elif lanjut == "y":
            os.system("clear")
            continue
        else:
            os.system("clear")
            print("Pilihan tidak ada")
            continue
        


def header():
    print("Pilihan".center(20,"="))
    [print(f"{index+1}.{i}") for index,i in enumerate(["Input DataSiswa","Tampil DataSiswa","Edit DataSiswa","Hapus DataSiswa","Exit"])]
    print("="*20)

def Mahasiswa():
    
    dSiswa = {}
    while True:
        header()
        pil = int(input("Pilih 1-5: "))
        if pil == 1:
            os.system("clear")
            print("Input Data".center(20,"-"))
            data_siswa = inputDt(dSiswa)
            dSiswa.update(data_siswa)
        elif pil == 2:
            os.system("clear")
            tampilDt(dSiswa)
        elif pil == 3:
            editDt(dSiswa)
        elif pil == 4:
            hapusDt(dSiswa)
        elif pil == 5:
            print("Akhir Program")
            break
Mahasiswa()