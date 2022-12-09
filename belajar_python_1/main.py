import os
import CRUD

def opsi():
    [print(f"{no+1}.{i}") for no,i in enumerate(["Read Data","Create Data","Update Data","Delete Data","Exit"])]

def header():
    print(f"{'=':=^40}")
    print("Program Database".center(40))
    print("Perpustakaan".center(40))
    print(f"{'=':=^40}")

def kondisi_pil(pil):
    if pil == 1:
        CRUD.read_data()
    elif pil == 2:
        CRUD.create_data()
    elif pil == 3:
        CRUD.update_data()
    elif pil == 4:
        print("4")
    elif pil == 5:
        return False

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")

    header()
    opsi()
    CRUD.check_db()
    e = input("Enter : ")

    while True:
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
        header()
        opsi()
        try :
            pil = int(input("\nMasukkan pilihan 1-5: "))
            if kondisi_pil(pil) == False:
                break

        except:
            print("pilihan harus angka! , silahkan input ulang")
            e = input("Enter : ")