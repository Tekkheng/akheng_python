# nasi goreng,nasi bakar,sate,kwetiaw
# es teh,es jeruk, thai tea, kopi

def header_makan():
    print("Menu Makanan".center(40,"=")+"\n")
    mkn = ["Nasi Goreng","Nasi Bakar","Kwetiaw","Sate"]
    price = [10000,15000,18000,20000]
    i = 0
    for m in mkn:
        i+=1
        print(f"{i}.{m} Rp.{price[i-1]:,}")

def header_minum():
    minum = ["Es teh", "Es jeruk", "Thai tea", "Kopi"]
    price = [4000,7000,1000,5000]
    i = 0
    for m in minum:
        i+=1
        print(f"{i}.{m} Rp.{price[i-1]:,}")

def makan(pil):
    blnj = int()
    if pil == 1:
        blnj += 10000
    elif pil == 2:
        blnj += 15000
    elif pil == 3:
        blnj += 18000
    elif pil == 4:
        blnj += 20000
    return blnj

def minum(pil):
    blnj = int()
    if pil == 1:
        blnj += 4000
    elif pil == 2:
        blnj += 7000
    elif pil == 3:
        blnj += 1000
    elif pil == 4:
        blnj += 5000
    return blnj

def akhir():
    confirm = input("mau pesan lagi? ketik yes or no: ")
    return confirm
def belanja():
    while True:
        header_makan()
        pil=int(input("pil: "))
        hasil_makan = makan(pil)
        print(f"Harga Makan : {hasil_makan}\n")
        header_minum()
        pil=int(input("pil: "))
        hasil_minum = minum(pil)
        print(f"Harga Minum : {hasil_minum}\n")

        tot = hasil_makan + hasil_minum
        print(f"Total Belanja : {tot:,}")

        hasil_akhir = akhir()
        if hasil_akhir == "yes":
            continue
        elif hasil_akhir == "no":
            break
        
belanja()