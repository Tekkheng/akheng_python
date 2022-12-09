import time
class Jam :
    def __init__(self,jam,menit,detik):
        self.jm = jam
        self.mnt = menit
        self.dtk = detik 


def tampil():
    print("Tugas Jam".center(30,"="))
    print("""
    {} Jam
    {} Menit
    {} Detik
    """.format(fcJam.jm,fcJam.mnt,fcJam.dtk))
    print("=".center(30,"="))

timeJ = time.localtime()
jam_t = time.strftime("%H",timeJ)
menit_t = time.strftime("%M",timeJ)
detik_t = time.strftime("%S",timeJ)
   
fcJam = Jam(jam_t,menit_t,detik_t)

tampil()


# class Jam :
#     def __init__(self,jam,menit,detik):
#         self.jm = jam
#         self.mnt = menit
#         self.dtk = detik 


# def tampil():
#     jam = int(input("Jam : "))
#     menit = int(input("Menit : "))
#     detik = int(input("Detik: "))

#     if jam <=24 and menit <= 59 and detik <= 59:
#         fJam = Jam(jam,menit,detik)
#         print("Tugas Jam".center(30,"="))
#         print("""
#         Jam : {}
#         Menit : {}
#         Detik : {}
#         """.format(fJam.jm,fJam.mnt,fJam.dtk))
#         print("=".center(30,"="))
#     else: 
#         print("Format Input Salah")
    
# tampil()

