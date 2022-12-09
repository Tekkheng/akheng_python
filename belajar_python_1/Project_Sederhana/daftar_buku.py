import os

def header():
    arry = ["input","see list_buku","edit","remove","exit"]
    no = 0
    print(" ")
    print("Program Buku".center(20,"="))
    for i in arry:
        no +=1
        print(f"{no}.{i}")
    print("=".center(20,"="))

def tampil_dt_siswa(list_buku):
    print(f"\n|{'No':^2}|{'Kode Buku':^12}|{'Judul Buku':^12}|{'Penulis Buku':^14}|{'Penerbit Buku':^14}|{'Tahun Terbit':^14}|")
    print("-"*75)
    if list_buku != []:
        for index,i in enumerate(list_buku):
            print(f"|{index+1:^2}|{i[0]:^12}|{i[1]:^12}|{i[2]:^14}|{i[3]:^14}|{i[4]:^14}|")
    else:
        print("DATA MASIH KOSONG")
    print("-"*75)

def input_dt():
    kode_buku = input("kode buku : ")
    judul = input("judul buku : ")
    penulis = input("penulis buku : ")
    penerbit = input("penerbit buku : ")
    tahun_terbit = input("tahun terbit : ")

    list_dt = [kode_buku,judul,penulis,penerbit,tahun_terbit]

    filter_hasil = [i for i in list_dt if i != ""]
    return filter_hasil

def hapus(list_bk):
    tampil_dt_siswa(list_bk)
    i_hapus = int(input("masukkan data index yang mau dihapus : "))

    list_bk.remove(list_bk[i_hapus-1])
    print("data berhasil di hapus")
    tampil_dt_siswa(list_bk)

    lanjut = input("Hapus Lagi ? y/n : ")
    if lanjut == "y":
        hapus(list_bk)
    elif lanjut == "n":
        os.system("clear")
    else:
        print("piihan tidak ada")
        hapus(list_bk)

def edit(list_bk):
    n = 0
    if list_bk == []:
        tampil_dt_siswa(list_bk)
        print("Data Masih Kosong, Input Data Dulu!")
        return
    else:
        while True:
            tampil_dt_siswa(list_bk)
            back = input("Lanjut Edit? y/n: ")
            if back == "n":
                os.system("clear")
                break
            elif back == "y":
                i_edit = int(input("masukkan index edit : "))
                lanjut = input("Index sudah sesuai? y/n: ")
                if lanjut == "y":
                    print("")
                    edit_list = list(input_dt())
                    list_bk[i_edit-1] = edit_list
                    print("\ndata berhasil di edit")
                    continue
                elif lanjut == "n":
                    os.system("clear")
                    continue
                else:
                    os.system("clear")
                    print("pilihan tidak ada")
                    continue
            else:
                os.system("clear")
                print("pilihan tidak ada")
                continue

def project_buku():
    list_buku = []
    while True:
        header()
        pil = int(input("masukkan Pilihan(1-5) : "))
        if pil == 1 :
            os.system("clear")
            print("Input Data".center(25,"="))
            hasil_input = list(input_dt())
            list_buku.append(hasil_input)
            tampil_dt_siswa(list_buku)
        elif pil == 2:
            os.system("clear")
            tampil_dt_siswa(list_buku)
        elif pil == 3:
            os.system("clear")
            edit(list_buku)
        elif pil == 4:
            os.system("clear")
            hapus(list_buku)
        elif pil == 5:
            break

project_buku()                                                    
        
