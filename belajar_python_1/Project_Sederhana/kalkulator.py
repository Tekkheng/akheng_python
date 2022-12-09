# kalkulator
import os

def header():
    arr = ["Pertambahan","Pengurangan","Perkalian","Pembagian","Exit"]
    print("Kalkulator".center(25,"="))
    for index,s in enumerate(arr):
        print(f"{index+1}.{s}")
    print("="*25)

def hitung(pil):
    print("Hitung".center(25,"-"))
    print("Masukkan Bilangan")
    bil1 = float(input("bil1: "))
    bil2 = float(input("bil2: "))
    if pil == 1:
        h=bil1+bil2
        st = "Pertambahan"
    elif pil == 2:
        h=bil1-bil2
        st = "Pengurangan"       
    elif pil == 3:
        h=bil1*bil2
        st = "Perkalian"      
    elif pil == 4:
        h=bil1/bil2
        st = "Pembagian"
    os.system("clear")
    print("Hasil".center(25,"-"))
    print(f"Bilangan 1 : {bil1}")
    print(f"Bilangan 2 : {bil2}")
    return h,st

def kalkulator():
    while True:
        header()
        pil = int(input("pilih 1-5: "))
        if pil == 5 :
            break
        elif pil < 5:
            os.system("clear")
            hasil = hitung(pil)
        else:
            print("pilihan tidak ada")
            continue
        
        print(f"Hasil {hasil[1]} : {hasil[0]}\n")

kalkulator()