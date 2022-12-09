from .operasi import create_first_data

DB_NAME = "data.txt"
TEMPLATE = {
    "pk" : "XXXX",
    "nim" : "",
    "nama" : 250*" ",
    "fakultas" : 250*" ",
    "tgl_lhr" : "",
    "created_at" : ""
}

def check_db():
    try:
        with open(f"CRUD/{DB_NAME}","r") as file:
            print("\ndata tersedia, init sukses!")
    except:
        with open(f"CRUD/{DB_NAME}","w",encoding="utf-8") as file:
            print("\ndata tidak ada, membuat data...\n")
            data = create_first_data()
            file.write(data)
            print("Data Berhasil Dibuat")
