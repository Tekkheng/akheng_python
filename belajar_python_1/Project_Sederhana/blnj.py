import os

def total_Bayar(total_mkn,total_minum):
    total = total_mkn + total_minum
    print(f"\nTotal Bayar Makan : Rp {total_mkn:,}")
    print(f"Total Bayar Minum : Rp {total_minum:,}")
    print("-".center(30,"-"))
    print(f"Total Bayar : Rp {total:,}\n")
    return total

def minum(h_minum):
    while True:
        hrg = menuMinum()
        pil = int(input("Pesan Minuman 1-7: "))
        if pil == 1 :
            h_minum += hrg[0]
        elif pil == 2 :
            h_minum += hrg[1]
        elif pil == 3 :
            h_minum += hrg[2]
        elif pil == 4 :
            h_minum += hrg[3]
        elif pil == 5 :
            h_minum += hrg[4]
        elif pil == 6 :
            h_minum += hrg[5]
        elif pil == 7 :
            h_minum += hrg[6]

        print(f"\nBelanja Minum : Rp {h_minum:,}")
        lanjut = input("pesan minum lagi? y/n : ")
        if lanjut == "y":
            os.system("clear")
            continue
        elif lanjut == "n":
            return h_minum
        else:
            os.system("clear")
            print("pilihan tidak ada")
            continue

def menuMinum():
    m_minum = ["Es Teh Manis","Es Teh Tawar","Es Jeruk","Juice Mangga","Coffe Panas","Juice Alpukat","Es Taro"]
    hrg = [5000,3000,7000,10000,6000,12000,9000]

    print("Menu Minum".center(30,"="))
    for index,i in enumerate(m_minum):
        print(f"{index+1}.{i} Rp.{hrg[index]:,} ")
    print("=".center(30,"="))

    return hrg


def makan(h_mkn):
    while True:
        h=menuMakan()
        pil = int(input("Pesan Makanan 1-7 : "))
        if pil == 1 :
            h_mkn += h[0]
        elif pil == 2 :
            h_mkn += h[1]
        elif pil == 3 :
            h_mkn += h[2]
        elif pil == 4 :
            h_mkn += h[3]
        elif pil == 5 :
            h_mkn += h[4]
        elif pil == 6 :
            h_mkn += h[5]
        elif pil == 7 :
            h_mkn += h[6]
        
        print(f"Belanja Makan : Rp {h_mkn:,}")
    
        lanjut = input("pesan makan lagi? y/n : ")
        if lanjut == "y":
            os.system("clear")
            continue
        elif lanjut == "n":
            return h_mkn
        else:
            os.system("clear")
            print("pilihan tidak ada")
            continue

def menuMakan():
    harga = [13000,20000,17000,18000,15000,12000,16000]
    m_mkn = {
        "Nasi Goreng" : harga[0],
        "KweTiaw" : harga[1],
        "Sate Ayam" : harga[2],
        "Ayam Geprek" : harga[3],
        "Bebek Goreng" : harga[4],
        "Ayam Penyet" : harga[5],
        "Ayam Bakar" : harga[6],
    }
    no = 0
    print("Menu Makan".center(30,"="))
    for k,m in m_mkn.items():
        no += 1
        print(f"{no}.{k} Rp {m:,}")
    print("=".center(30,"="))
    return harga


def header():
    dftr=["Belanja Makan","Belanja Minum","Total Bayar","Exit"]
    print("Belanja".center(30,"="))
    for index,i in enumerate(dftr):
        print(f"{index+1}.{i}")
    print("=".center(30,"="))

def menu():
    total_mkn = 0
    total_minum = 0
    tot = 0
    while True: 
        h_mkn = 0   
        h_minum = 0
        header()
        pil = int(input("\npilihan : "))
        print(" ")
        if pil == 1:
            os.system("clear")
            h_mkn = makan(h_mkn)
            total_mkn += h_mkn
            tot += h_mkn
            total_Bayar(total_mkn,total_minum)
        elif pil == 2:
            os.system("clear")
            h_minum = minum(h_minum)
            total_minum += h_minum
            tot += h_minum
            total_Bayar(total_mkn,total_minum)
        elif pil == 3 :
            os.system("clear")
            total_Bayar(total_mkn,total_minum)
        elif pil == 4 :
            break
            
menu()    