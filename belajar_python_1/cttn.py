#===============================================================================================================
#### comment pada python3 #### : 
# 1.pagar => #
# 2 """ISI KOMEN""" atau '''ISI KOMEN'''

#===============================================================================================================
#### \n, \t, " '' ", \b ####
# \n untuk enter new line
# \b backspace
# \t tab
# " '' " petik

# print(" how is\'it today, is it 'good' ?\t hehe\nmantab ")

# menggunakan raw string:
# r"" # smeua yg ada didalam r akan di print sebagai string sehingga fungsi \n \t \b tidak ada hanyak ditampilkan sebagai string
# print(r"C:\new folder \b \t \n")

#===============================================================================================================
#### 6 type data #### :
# 0 = False
# >1 = true

# 1.str(),  2.int(),   3.bool(),   4.float(),   5.complex(5,6),   6.c_double(10.5)
# type("23"), type(23), type(True), type(23.53) type(complex(5,6)), type(c_double(10.5))

# type data dri bahasa C :
# from ctypes import c_double
# d_c_double = c_double(10,5)

# Casting type Data:
# str(23), int("23"), bool(1), float(23)

#===============================================================================================================
#### 3 cara penulisan string #### :
# age = 20
# b = True
# height = int(74.5)

# cara 1 :
# print("Nama: "+"Akheng\n"+ "Umur: "+str(age)+"\ntinggi: "+str(height)+" = "+str(b))

# cara 2 :
# print(f"Nama: Akheng\nUmur:{age}\ntinggi:{height} = {b} ")

# cara 3 :
# print("Nama : Akheng\nUmur:{}\ntinggi:{} = {}".format(age,height,b))

# cara multiline :
# print(f"""
# nama : {age}
# umur : {age}
# tinggi : {height} = {b}    
# """)
#-----------------------------
## cara multiline Format ## :
# print(f"""
# nama : Akheng
# umur : {{}}
# tinggi : {{}} = {{}}   
# """.format(age,height,b))

#===============================================================================================================
#### cara ambil input data dari user #### :
# nama = input("Nama: ")
# umur = int(input("Umur : "))
# tinggi = float(input("Tinggi: "))
# t_o_f = bool(int(input("True or False: "))) # masukan angka 0=false,  >1 = True

# print(f"Hasil : {nama},{umur},{tinggi},{t_o_f}")
#===============================================================================================================
# print simpel
# t = "&"
# print("+".center(20,"+"))
# print("+"*20)
# print(f"{'pesan':=^20}")

# print(t.center(20,"+"))
# print(t*20)
# print(f"{t:-^20}")
#===============================================================================================================
#### Aritmatika #### :
# tambah,kurang,kali,bagi,eksponen(pangkat),modulus,floor Division
# +, -, *, **, /, %, //
#-----------------------------------------------------------------------------------------------------------------
# a = 9
# b = 2
# h = a+b
# h = a-b
# h = a*b
# h = a**b # a Pangkat b
# h = a/b
# h = a%b # ambil sisa bagi 9/2 = 4, sisa 1, hasil = 1 
# h = a//b # kebalikan dari modulus buang sisa, 9/2 = 4, sisa 1, hasil = 4
#-----------------------------------------------------------------------------------------------------------------
## Prioritas Operator ## :
# 1. tanda kurung () # => (a+b)*c => yg dihitung duluan a + b
# 2. eksponen/pangkat
# 3. *,/,%,//
# 4. + dan -

#===============================================================================================================
#### Operasi Komparasi / Perbandingan if, else, else if(elif) #### :
# >, <, >=, <=, ==, !=, is, is not
# a = 4
# b = 2

# if a > b    # 4 > 2 -> True
# if a >= b   # 4 >= -> True
# if a < b    # 4 < 2 -> False
# if a <= b   # 4 <= 2 -> False
# if a == b   # 4 == 2 -> False
# if a != b   # 4 != 2 -> True

# if a is b  -> False
# if a is not b -> True

# is dan # is not hanya untuk membandingkan object variabel seperti a dan b, tidak untuk, cth: 5 is 2
#-------------------------------------------------------------------------------------------------------------------
## Operasi Boolean ## :
# or,and,xor -> ^ ,not
# a = False
# b = True

# if a or b: # True karena bila salah satu True maka nilai True, a = false,tetapi b = True
#     print("tampil or")
# if a and b: # False karena bila salah satu False maka nilai False, kedua2nya harus True untuk -> and dijalankan
#     print("tampil and")
# if a ^ b: # True karena bila salah satu True maka nilai True, syarat = salah satu harus True dan tidak boleh kedua2 ny True
#     print("tampil xor")

# not untuk mengubah nilai menjadi kebalikannya dari false menjadi true, dan true menjadi false
# h = not a # a yang awal ny False akan menjadi True
# h1= not b # b yang awal ny True akan menjadi False
# print(h,h1) # Output => True,False

#-----------------------------------------------------------------------------------------------------------------
## CTH Perbandingan IF ELSE ## :
# dt = int(input("angka: "))

# # -----0++++++5-----8++++11------
# if (dt > 0 and dt <=5) or (dt >=8 and dt <=11) :
#     print("HASIL : TRUE")
# else:
#     print("HASIL : FALSE")
#-----------------------------------------------------------------------------------------------------------------
## contoh if elif else ## : 
# nama = input("ISI NAMA : ")
# def controlFlow():
#     if (len(nama) > 5 and len(nama) < 8):
#         print("5 ++++ 8")
#     elif len(nama) < 5 and len(nama)>1:
#         print("<5")
#     elif len(nama) <= 1:
#         print("end")
#     elif len(nama) == 5:
#         print("5 woi")
#     else:
#         print("NOTHING")
# controlFlow()

#===============================================================================================================
#### Pengulangan atau looping for and while #### :
# FOR -> UNTUK LOOP YG SUDAH DIKETAHUI JUMLAH BATASNYA
# FOR -> LOOP STRING
# var1 = "tekkheng"
# for i in var1:
#     print(i)
#-----------------------------------------------------------------------------
## FOR -> LOOP ARRAY ##
# arr = ["hi","apa","kabar","no",str(20)]
# tampung = ""
# for i in arr:
#     tampung += i + " "
#     print(tampung)
#-----------------------------------------------------------------------------
## FOR -> LOOP RANGE() ##
# for i in range(10):
#     print(f"{i+1}.{i}")
#-----------------------------------------------------------------------------
# for i in range(1,11):
#     print(i)

# For
# count = 1
# for i in range(11):
#     print("*"*count)
#     count +=1

#     if count > 10:
#         for i in range(11):
#             print("*"*count)
#             count -= 1
#-----------------------------------------------------------------------------
## WHILE LOOP ##
# count = 1 
# while count < 10:
#     print("*"*count)
#     count +=1    

# count = 10 
# while count > 0:
#     print("*"*count)
#     count -=1 

# count = 1
# while True:
#     print(count)
#     count += 1
#     if count > 10:
#         break


# n = 24
# count = 1
# while True:
#     if count < n:
#         if count % 2:
#             print("+"*count)
#             count+=1    
#         else :
#             count += 1
#             continue
        
#         if count >= 24:
#             count -=2
#             while True:
#                 if count < 1:
#                     break
#                 if count % 2:
#                     print("+"*count)
#                     count -=1
#                 else:
#                     count -= 1
#                     continue
#         if count < 1 :
#             break
#-----------------------------------------------------------------------------

# count = 1
# while count < 10 and count > 0:
#     print("*"*count)
#     count+=1
#     if count == 10:
#         while True: 
#             count -=1
#             print("*"*count)
#             if count < 1:
#                 break

#===============================================================================================================
## ljust(),rjust(),center(), dan cara print string,variabel dengan space logo(=,.*+dll) atau tidak ##
# .strip() => menghilangkan sesuatu contoh hilangkan = dengan .strip("=")

# print("Header".center(20,"=")) # output -> =====Header=====
# print("Header".ljust(20,"=")) # output ->  Header==========
# print("Header".rjust(20,"=")) # output ->  ==========Header
# # print("Header".center(20," ")) # isi dari center(20," ") => petikny bebas di isi apa, klw kosong hanya tab
# ---------------------------------------------------------------------------------------------------------------

# a = 1000
# b = "akheng"
# # print("wkwk"*10) #output -> wkwkwkwkwkwkwkwkwkwk
# print(f"{a:,.2f}") #output -> 1,000.00 -> :, untuk kasih tanda koma didepan dan :.2f untuk memberi 2 koma di belakang angka
# print(f"{a:.2%}") #output -> 100000.00% -> :.2% untuk % dengan 2 belakang koma -> :.2% untuk mengubah menjadi %

# print(f"{b:=>10}") #output -> ===========akheng
# print(f"{b:.<10}") #output -> akheng......
# print(f"{b:-^10}") #output -> ----akheng----
# print(f"{b:^10}") #output ->      akheng

#===============================================================================================================
# tes="akheng testing"
# len(tes) -> menghitung length dari tes

# tes.count("e") -> menghitung jumlah huruf

# upper(), isupper()
# lower(), islower()
# title(), istitle()

# a = "aKheNg"
# b = "akHeNg teSt"
# print(a.upper())
# print(a.lower())
# print(b.title())
# # isupper , islower, istitle mengecek apakah stringny huruf besar semua,huruf kecil semua, huruf pertama besar atau tidak,jika iya maka True
# print(a.isupper())
# print(a.islower())
# print(a.istitle())

# min()
# max()
# .isalpha() ---> untuk mengecek semuany huruf(tidak boleh spasi)
# .isalnum() ---> untuk mengecek ada huruf dan angka
# .isdecimal() ---> untuk mengecek ada angka saja
# .isspace() ---> untuk mengecek ada/tidak ada spasi tab newline\n
# .casefold() --> mengembalikan semua karakter dimana semua karakter huruf kecil
# .startswith() -> akan True bila data ny ada yg sama cth variabel tes="hai tes" => tes.startswith("hai")
# .endswith() -> akan True bila data ny ada yg sama cth variabel tes="hai tes" => tes.endswith("tes")
# .join()
# .split()

#===============================================================================================================
## Date And Time ##

# import datetime as dt

# print("Hitung Umur".center(30,"="))
# tgl = int(input("Tanggal Lahir: "))
# bulan = int(input("bulan Lahir: "))
# tahun = int(input("Tahun Lahir: "))

# tgl_lahir = dt.date(tahun,bulan,tgl)
# tgl_now = dt.date.today()

# umur = tgl_now - tgl_lahir
# umur_thn = umur.days // 365
# umur_bln = int((umur.days % 365) / 30) 
# umur_hari = int((umur.days % 365) % 30)
# print(f"hari pada saat anda Lahir adalah : {tgl_now:%A}")
# print(f"Tanggal Lahir: {tgl_lahir}")
# print(f"Tanggal Sekarang: {tgl_now}")
# print(f"Umur Anda : {{}} Tahun, {{}} Bulan, {{}} Hari".format(umur_thn,umur_bln,umur_hari))

#===============================================================================================================
#### LIST(mirip Array) ####

# dt = [5,"tek","halo",True,"haha","4",False]
# print(dt)

# print(f"index 2 : {dt[2]}")
# print(f"length : {len(dt)}")
#------------------------------------------------------------------------------------------------------------------------
## mengubah dt range menjadi list ## :
# dt_range = range(1,11)
# dt_list = list(dt_range)
# print(f"dt_list : {dt_list}")
#------------------------------------------------------------------------------------------------------------------------
## list for loop ##
# list_dt = [4,"h",7,"wo","good"]
# list_for = [i for i in range(1,11)]

# fungsi list dari variabel adalah i ny bisa di manipulasi seperti i**2 i*2 jadi setiap indexny akan di kalikan
# contoh :
# list_cth = [i*2 for i in range(1,11)] => setiap indexny dikalikan 2
# print(f"list Cth : {list_cth}")

# list_for2 = [i for i in list_dt]
# print(list_for)
# print(list_for2)

#------------------------------------------------------------------------------------------------------------------------
## list pake for pake if ## :
# cara simpel :
# dt_angka = [i*2 for i in range(2,11) if i % 2 ]
# print(dt_angka)

# listdt = [3,6,9,12]
# tmpng = [int(i/3) for i in listdt]
# print(tmpng)


# # cara ribet :
# h = [2,3,4,5,6,7,8,9,10]
# tmpng = []
# for i in h:
#     if i % 2 :
#         tmpng += str(i)
#     else :
#         continue
# print(tmpng)

# # int dalam array
# t = []
# for i in h :
#     t += [int(i**2)]
# print(t)

# # str dalam array
# t = []
# for i in h :
#     t += [f"{i**2}"]
# print(t)
#------------------------------------------------------------------------------------------------------------------------
#### MENAMBAH DATA PADA LIST(ARRAY) ####
# pake .insert(index,isi) atau dengan .append(isi) => append hanya untuk menambahkan di akhir list seperti appendChild in javascript
# .extend(dt) menggabungkan array
# .insert(index,isi) .append(isi)
# dt[index] = " " => edit
# .pop() => hapus data list paling akhir
# .remove(isi) hapus data list yang mau dihapus
# .index(isi) => mencari index isi dari data tersebut
# .count(isi) => menghitung jumlah isi ada berapa di data tersebut contoh menghitung angka 2 ada berapa angka 2 di data array itu
# .sort() => mengurutkan array, bila angka akan diurutkan dari 1,2,3,dll, jika string akan diurutkan dari abjad huruf pertama
# .reverse() => di terbalikan urutan arrayny
# .copy() => copy data array ke array baru yg ditampung dengan variabel baru

## var.insert(posisi,dtygdmaudimasukin)

# dt1 = ["selamat","pagi","apa","kabar"]
# dt1.insert(4,"akheng")
# dt1.insert(0,"hai")
# dt1.append("akhir")
# dt1.remove("pagi")

# print(dt1)

# tmpl = " "
# for i in dt1 :
#     tmpl += i+" "

# print(tmpl)
#------------------------------------------------------------------------------------------------------------------------
## menggabungkan array dengan array lain:
# arr1 = ["selamat","pagi"]
# arr2 = ["semua","manusia"]
# arr1.extend(arr2)
# print(arr1)

# ## merubah data :
# arr1[3] = "monster"
# print(arr1)

# ## menghapus data:
# arr1.remove("pagi")
# arr2.pop()
# print(arr2)
# print(arr1)


# data_angka = [1,5,6,3,2,7,3,5,1,6,8,1]
# h = data_angka.count(1)
# print(f"jumlaha angka 1 : {h}")

# str_dt = ["ucup","don","ddia","yesa"]
# i_ddia =str_dt.index("ddia")
# print(f"nama ddia berada di index : {i_ddia}")

# data_angka.sort()
# print(f"sudah di urut dengan sort : {data_angka}")

# dt = ["woiip","haha","io"]
# dt.sort(key=len)
# print(f"dt sort by len : {dt}")

# data_angka.reverse()
# print(f"sudah di reverse dengan reverse() : {data_angka}")

#--------------------------------------------------------------------------------------------------------------
## copy/clone list(array) ##
# a = ["kemarin","ulangan","mtk","di","sekolah"]

# # copy list yg tidak disarankan : 
# b = a 

# # copy list yg benar :
# c = a.copy() # clone data array yg benar, dijavascript seperti c = [...a]
# print(f"a original : {a}")
# a[0] = "besok"
# print(f"a setelah diubah : {a}")
# print(f"b ikut berubah : {b}") # data b ikut terubah
# print(f"c : {c}")

#--------------------------------------------------------------------------------------------------------------
## NESTED LIST ## :

# list_1 = [3,2,5]
# list_2 = [1,4,8]

# list_2D = [list_1,list_2]


# print(f"list_2D : {list_2D}")
# print(f"list_2D index ke 1 : {list_2D[1]}")
# print(f"list_2D index ke 1 array ke 2 : {list_2D[1][2]}\n")

# for i in list_2D:
#     print(f"{i[2]}")

#--------------------------------------------

# list_str1 = ["Tek kheng",20,"laki-laki"]
# list_str2 = ["Yesa",19,"Perempuan"]

# list_data = [list_str1,list_str2]
# print(list_data)
# for i in list_data:
#     print(f"""
#     Nama : {i[0]}
#     Umur : {i[1]}
#     """)


# lob = {
#     "nama":"Tekkheng",
#     "umur":20,
# }

# list_tes = [list_1,lob]
# print(f"list_tes array ke 1 yg object: {list_tes[1]}")

# menggunakan deepcopy :
# masalah copy ketika menggunakan

# list_dt = [3,2,5]
# list_dt2 = [1,4,8]

# list_2D = [list_dt,list_dt2]
# #copy luar saja tetapi didalamny bisa ikut terubah maka dari itu membutuhkan deepcopy
# clone_list_2D = list_2D.copy()  

# list_2D2 = [list_dt.copy(),list_dt2.copy()] # tidak disarankan karena, hanya untuk nested yg sedikit klw banyak membutuhkan deepcopy
# list_dt[1] = 10
# print(clone_list_2D) # ikut terubah ketika list_dt diubah
# print(list_2D2) # tidak terubah, mencopy list dalam nested dengan .copy tetapi jika banyak jadi harus satu2 dan tidak disarankan,solusi menggunakan deepcopy

# # deep copy untuk copy nested list:
# from copy import deepcopy
# list_2D_nested = [list_dt,list_dt2]
# list_deepcp = deepcopy(list_2D_nested)

# list_2D_nested[1][2] = 12 # list_2D_nested[1] diubah tetapi list_deepcp tidak terubah karna menggunakan deepcopy

# print(f"list_2D_nested: {list_2D_nested}")
# print(f"list_deepcp: {list_deepcp}")

#---------------------------------------------------------------------------------------------
# looping list

# dt = ["akheng","pagi","selemat","hello"]
# dt_2 = [5,7,1,4,2,9,7,2]
# tmpng = " "

# for i in dt:
#     tmpng += i + " "


# for angka in dt_2:
#     print(angka)

# print(tmpng)


# for i in range(len(dt)) :
#     print(dt[i])

# i = 0
# while i < len(dt_2):
#     print(dt_2[i])
#     i += 1



# list comprehension
# arr_dt = ["tek",5,"pagi",7,8]
# arr2 = [6,7,3,5,3,"akhir"]
# tes = [i for i in arr_dt if len(arr_dt) > 1]
# print(tes)

# [print(f"data : {i*2}") for i in arr2]

# # enumerate :
# print(f"Enumerate".center(30,"="))
# for var_index, var_arr2 in enumerate(arr2):
#     print(f"index = {var_index} arr2 = {var_arr2}")


# Daftar Buku - Latihan List  
# def input_dt():
#     inpt_judul = input("Masukkan Judul Buku : ")
#     inpt_penulis = input("Masukkan Nama Penulis: ")
    
#     buku_baru = [inpt_judul,inpt_penulis]
#     return buku_baru
  

# def buku():
#     list_buku = []
#     while True : 
#         data_buku = ["No","Judul Buku","Penulis"]
#         buku_input = input_dt()
        
#         if buku_input[0] != "" and buku_input[1] != "":
#             list_buku.append(buku_input)

#         print(f"| {data_buku[0]} | {data_buku[1]} | {data_buku[2]} |")

#         for index,buku in enumerate(list_buku):
#             print(f"| {index+1}\t{buku[0]}\t{buku[1]} | ")
        
#         lanjut = input("mau lanjut?(y/n) : ")

#         if lanjut == "n" :
#             print("akhir Program")
#             break
#     # print(list_buku)
# buku()

#===================================================================================================================
#### Tuples dan Set #### :
# import array as arr
# hh = arr.array([2,"dd"])
# print(hh)

## data Tuples => ()
# tidak bisa diubah datany dengan apapun => append,insert,pop semua tidak berfungsi
# tuples_tes = (2,5,3,4,"oi",True,9,2)
# print(tuples_tes)
# print(tuples_tes[3])
# tuples_tes(4) = "dt_baru" => # akan error karena datany tidak bisa diubah hanya bisa diakses

#---------------------------------------------------------------------------------------------------
## data set(himpunan) => data set tidak memiliki index {}
# data set dipakai hanya untuk menghitung sesuatu

# set_tes = {5,7,2,9,4,"oi",True,6,9}
# print(set_tes)
# # print(set_tes[5]) # => akan error karena tidak ada index
# set_tes.append("hai")
# print(set_tes)

#=================================================================================================================
##### dictionary ####
# list_tes = [5,"hai","tes",False,9]
# kamus = {
#     "nama" : "tek",
#     "umur" : 25,
#     "type" : True,
#     "dt_list" : list_tes,
#     "tes" : [0,6,72,23],
# }
# print(kamus)
# # dua cara akses data dictionary :
# # satu : 
# print(kamus["nama"])
# # dua :
# print(kamus.get("nama"))
# #

# print(kamus["dt_list"][1])
# print(kamus["tes"])
# print(kamus.get("tes"))

# # disarankan menggunakan .get() dibanding kamus["nama"]
# print(kamus.get("agama","data tidak ada di kamus")) # kelebihan bisa kasih data default di argument ke 2, bila data di kamus tidak ditemukan
#-------------------------------------------------------------------------------------------------------------------------------------
## mengambil length dictionary dan mengecek data didalam dicitonary apakah ada, + mengupdate dan menambah data di dicionary
# list_tes = [5,"hai","tes",False,9]
# kamus2 = {
#     "nama" : "tek",
#     "umur" : 25,
#     "type" : True,
#     "dt_list" : list_tes,
#     "tes" : [0,6,72,23],
# }
# # length
# TES = len(kamus2)
# print(f"Pnjng Dt : {TES}")

# # cekdt
# checkdt = "type" in kamus2
# print(f"apakah type ada di dalam kamus2? = {checkdt}")

# ## data otomatis di add bila tidak ada data yg sama,jika ada data yang sama maka di edit isiny
# # cara 1:
# # edit data nama di dicitonary kamus2
# kamus2["nama"] = "akheng" 
# print(kamus2.get("nama"))

# # menambah data di dicitonary kamus2
# kamus2["agama"] = "budha"
# print(kamus2)

# # cara 2 :
# # edit data nama di dicitonary kamus2
# kamus2.update({"nama":"manusia"})
# print(kamus2.get("nama"))

# # menambah data di dicitonary kamus2
# kamus2.update({"nim":20210801205})
# print(kamus2)

#-----------------------------------------------------------------------------------------------------------------------
## looping Dictionary ##
# .keys(), .values(), .items()

# dt_dict = {
#     "nama" : "asup",
#     "umur" : 25,
#     "kelas" : "5a",
# }

# tes_key = dt_dict.keys()
# print(tes_key)

# tes_value = dt_dict.values()
# print(tes_value)


# # loop keyny("nama","umur","kelas") :
# for dt in dt_dict:
#     print(dt)
# print("\n")

# # loop valuesnya : 
# # keys() => masuk ke keys => key adalah "nama","umur","kelas pada dt_dict diatas" 
# for dt in dt_dict.keys(): # masuk ke keys
#     print(dt_dict.get(dt)) # kemudian looping valueny

# for dt in dt_dict.values():
#     print(dt)
# print("\n")

# # items => berisi gabungan dari key dan value 
# dt_items = dt_dict.items()
# print(dt_items)
# print("\n")

# for i in dt_dict.items():
#     print(i) 
# print("\n")

# # cara simpel :
# for k,v in dt_dict.items():
#     print(f"keys : {k}, valuesny : {v}")

#-----------------------------------------------------------------------------------------------------------------------
## copy & pop dictionary ##
# .copy(), .pop()

# copy :
# data_buku = {
#     "judul" : "sangkuriang",
#     "nomor_buku" : 232323,
#     "penulis" : "andi",
#     "penerbit" : "yasa",
#     "key_arr": ["hh","mm","ww"]
# }

# clone_dt = data_buku.copy()
# data_buku.update({"penulis":"tonia"})

# print(f"data clone copy aman: {clone_dt.items()}\n")
# print(f"data original yg terubah: {data_buku.items()}\n")

# # pop() => berdasarkan (keyny):
# dt_pop = data_buku.pop("nomor_buku") # menghilangkan data nomor_buku
# print(dt_pop)
# print(data_buku)

# # popitem() => data yang terakhir aja
# data_buku.popitem() # menghilangkan data akhir
# print(data_buku)

#-----------------------------------------------------------------------------------------------------------------
## multikey dictionary ## :
# import datetime as dt
# mhs = {
#     'nama':'tek',
#     'nim' : '193023',
#     'sks_lls' : 130,
#     'beasiswa' : False,
#     'date' : dt.datetime(2002,1,17)
# }

# print(mhs.get('date'))
#-----------------------------------------------------------------------------------------------------------------
## Nesting dictionary ## :

# import datetime as dt
# mhs1 = {
#     'nama':'tek',
#     'nim' : '193023',
#     'sks_lls' : 130,
#     'beasiswa' : False,
#     'date' : dt.datetime(2002,1,17)
# }
# mhs2 = {
#     'nama':'akheng',
#     'nim' : '38522',
#     'sks_lls' : 90,
#     'beasiswa' : False,
#     'date' : dt.datetime(2005,10,5)
# }
# mhs3 = {
#     'nama':'ucup',
#     'nim' : '5282',
#     'sks_lls' : 119,
#     'beasiswa' : True,
#     'date' : dt.datetime(2001,3,12)
# }

# dt1 = {
#     'key1' : mhs1,
#     'key2' : mhs2,
#     'key3' : mhs3,
# }

# print(f"{'KEY':^6} {'NIM':^8} {'NAMA':^8} {'SKS':^8} {'Beasiswa':^8} {'Lahir':^8}")
# print('-'*50)
# # for k,i in dt1.items():
# #     print(k,i)
# for i in dt1.keys():
#     KEY = i
#     # DT = dt1[KEY]["nama"]
#     NAMA = dt1.get(KEY)['nama']
#     NIM = dt1.get(KEY)['nim']
#     SKS = dt1.get(KEY)['sks_lls']
#     BEASISWA = dt1.get(KEY)['beasiswa']
#     DATE = dt1.get(KEY)['date'].strftime("%x")

#     # print(f"{'{}'} {'{}':^6} {'{}':^10} {'{}':^10} {'{}':^10} {'{}':^10}".format(KEY,NIM,NAMA,SKS,BEASISWA,DATE))
#     print(f"{KEY:^6} {NIM:^8} {NAMA:^8} {SKS:^8} {BEASISWA:^8} {DATE:^8}")

#===============================================================================================================
# def(function python])

# nama = "Akheng"
# umur = 20

# def nama_function(nama,umur):
#     print(f"Selamat Siang nama saya {nama}, saya berumur {umur} ")
#     a = 2
#     b = 3
#     h = a * b
#     return h

# h = nama_function(nama,umur)
# print(f"h = {h}")

#-----------------------------------------------------------------
# a = 10
# b = 2
# def hitung(a,b):
#     tmb = a + b
#     krg = a - b 
#     kali = a * b
#     bagi = a / b
#     return tmb,krg,kali,bagi

# tmb,krg,kali,bagi = hitung(a,b)
# print(tmb)
# print(krg)

# hasil = hitung(a,b)
# print(hasil)

# default argument :
# def fungsi1(nama = "yukp",):
#     print(f"Namaku: {nama}")
# fungsi1()

# def fungsi(angka1,nama = "tek",):
#     print(f"Namaku: {nama}, {angka1}")
# fungsi(80)

# def hitung(a=3,b=5,c=1,d=9):
#     hasil = a + b + c + d
#     return hasil
# hasil = hitung(c=7) # Mengubah nilai default c dari 1 menjadi 7
# print(hasil)
#-----------------------------------------------------------------
# membuat program dengan rapi dengan menggunakan function2/def
# import os

# def header():
#     print("")
#     print("+"*40)
#     print(f"{'Program Menghitung Luas':^40}")
#     print("Dan Keliling Persegi Panjang".center(40))
#     print("+"*40)
    
#     print("")
#     arr = ["Hitung Luas","Hitung Keliling"]
#     for index,i in enumerate(arr):
#         print(f"{index+1}.{i}")

# def inputUser():
#     LEBAR = int(input("\nMasukkan Nilai Lebar : "))
#     PANJANG = int(input("Masukkan Nilai Panjang : "))
#     return LEBAR,PANJANG

# def hitung_keliling():
#     while True :
#         os.system("clear")
#         print(f"Hitung Keliling".center(40,"-"))
#         p,l = inputUser()
#         keliling = 2*(p+l)
#         tampil("\nHasil Hitung Keliling : ",keliling)
#         lagi = input("Lanjut hitung Keliling? y/n : ")

#         if lagi == "n":
#             os.system("clear")
#             return keliling
#         else: 
#             continue

# def hitung_luas():
#     while True:
#         os.system("clear")
#         print(f"Hitung Luas".center(40,"-"))
#         p,l = inputUser()
#         luas = p * l
#         tampil("\nHasil Hitung Luas : ",luas)
#         lagi = input("Lanjut hitung luas? y/n : ")

#         if lagi == "n":
#             os.system("clear")
#             return luas
#         else:
#             continue
        

# def do_Hitung():
#     pil = int(input("\nPilih : 1-2: "))
#     if pil == 1:
#         luas = hitung_luas()
#         return luas
#     elif pil == 2:
#         keliling = hitung_keliling()
#         return keliling

# def tampil(pesan,isi):
#     print(f"{pesan} : {isi}")

# def main():
#     while True:
#         header()
#         print("")
#         hasil = do_Hitung()
    
#         lagi = input("\nlanjut menghitung? y/n : ")
#         if lagi == "y":
#             os.system("clear")
#             continue
#         elif lagi == "n":
#             print("Program Selesai")
#             break
#         else : 
#             os.system("clear")
#             print("Pilihan tidak ada")
#             continue
# main()
#===============================================================================================================
# Type Hints pada fungsi(def) :

# def pngkt(argument:int):
#     output = 10**argument
#     return output
# output = pngkt(5) # fungsi argument:int untuk memberi hints/info ketika output = pngkt(5) di hover akan memeberitau type data yang harus di input(argument -> int)
# print(output)

#====================================================================================================================
#### args #####
# cara normal
# def dt(tinggi,berat):
#     print(f"tinggi = {tinggi}, berat = {berat}")
# dt(170,45)

# dengan args * :

# def lat(*data):
#     bil1 = data[0]
#     bil2 = data[1]
#     hasil = data[2]
#     output = bil1 * bil2
#     print(f"{hasil} dari {bil1} x {bil2} adalah {output}")
# lat(5,7,"hasil")

# def tes(*data):
#     total = 0
#     for i in data:
#         total += i
#     print(f"total : {total}")
# tes(6,9,1,5,3,8,5,6,2)
#--------------------------------------------------------------------------------------
#### kwargs #####
# kwargs menangkap data menjadi dictionary
# def fungsi(**data):
#     tinggi = data.get("tinggi")
#     berat = data.get("berat")
#     print(f"{data.get('nama')} dengan tinggi : {tinggi} dan berat : {berat}")
# fungsi(nama="tek",tinggi=77,berat=55)

## args + kwargs ##
# def campur(*dt,**data):
#     nilai = 1
#     if data.get("operator") == "tambah":
#         for i in dt:
#             nilai += i
#         print(f"tambah : {nilai}")
#     elif data["operator"] == "kali":
#         for i in dt:
#             nilai *= i
#         print(f"kali : {nilai}")
# result = campur(5,6,8,operator = "tambah")
# result = campur(5,6,8,operator = "kali")

## lambda ##
# lambda parameter : expresion

# cara normal
# def fngsi(*dt):
#     print(f"{dt[0]} pangkat {dt[1]} adalah {dt[0]**dt[1]}")
# fngsi(5,4)

# fcld = lambda a,b : (a * 2)/b
# result = fcld(9,6)
# print(result)

# # cara lambda lebih singkat
# kuadrat = lambda angka:angka**4
# print(kuadrat(5))

# # lambda with args *
# kuadrat = lambda *angka : angka[2]**4
# print(kuadrat(5,9,7))

# # lambda dengan 2 argument
# pangkat = lambda angka1,angka2 : angka1 ** angka2
# print(pangkat(5,4))


# kuadrat = lambda angka : angka**2
# hasil = kuadrat(5)
# print(hasil)

# dt1 = [5,6,8,2,1,9,3]
# # filter dengan lambda
# dt_baru = list(filter(lambda x:x<5,dt1))
# print(dt_baru)
# # filter dengan function biasa
# def fc_dt(angka):
#     return angka < 5

# dt_baru = list(filter(fc_dt,dt1))
# print(dt_baru)
#===============================================================================================================
# Global dan Local scope
# cara mengakses global angka dari dalam function ubah yang merupakan local scope
# angka = 0
# def ubah():
#     dt = [5,4,6,7]
#     for index,i in enumerate(dt):
#         global angka
#         angka += i
# ubah()
# print(angka)
#+===============================================================================================================
#### import statement ####
# import os
# os.system("clear")

# # import nama_file => file external .py
# import tes_import
# print(f"Nama = {tes_import.nama}")
# hasil_tambah = tes_import.tambah(5,6)
# print(f"hasil tambah = {hasil_tambah}")

# alias :
# import nama_file as nf => file external .py
# print(nf.nama)

# from nama_file import umur as age
# print(age)

#--------------------------------------------------
# from nama_file import variabel/function/etc => file external .py
# from tes_import import tambah,nama
# print(f"Nama = {nama}")
# hasil_tambah = tambah(5,6)
# print(f"hasil tambah = {hasil_tambah}")

# # from nama_file import * => file external .py   import semua dengan *
# from tes_import import *
# print(f"Nama = {nama}")
# hasil_tambah = tambah(5,6)
# print(f"hasil tambah = {hasil_tambah}")

# def campur(*dt,**data):
#     nilai = 1
#     if data.get("operator") == "tambah":
#         for i in dt:
#             nilai += i
#         print(f"tambah : {nilai}")
#     elif data["operator"] == "kali":
#         for i in dt:
#             nilai *= i
#         print(f"kali : {nilai}")
# result = campur(5,6,8,operator = "tambah")
# result = campur(5,6,8,operator = "kali")

#### membuat module + init + main #### :
# __pycache__ auto dibuat ketika mengimport suatu module
# buat folder akheng
# buat file __init__.py didalam folder akheng => supaya lebih rapi
# buat file __main__.py didalam folder akheng =>
# buat file kalkulator.py di dalam folder akheng

# buat folder hitung_gaya didalam folder akheng: didalam ny isi dengan: 
# file fisika.py dan __init__.py 

# didalam folder hitung_gaya pada file __init__.py import yg dibutuhkan cth :
# chaining dengan :
# from .fisika import gaya 

# dan __init__.py yang satuny,yg terletak didalam folder akheng isi dengan import yg dibutuhkan cth:
# from .kalkulator import tambah,kali,bagi,kurang

#------------------------------------------
## cara normal :
# import sains.fisika # import folder(module) sains dengan file fisika.py
# from sains.fisika import gaya # dari module sains dengan file fisika.py import fungsi gaya
# hasil_tambah = sains.mtk.tambah(5,6)
# hasil_kali = sains.mtk.kali(5,5)
# print(f"hasil penjumlahan : {hasil_tambah}")
# print(f"hasil perkalian : {hasil_kali}")

## ketika menggunakan file __init__.py => berfungsi membuat modul menjadi lebih rapi dan terstruktur
# cukup import module dan import file2 .py yang dibutuhkan ke __init__.py supaya lebih rapi
# from .fisika import gaya => di file __init__.py atau from . import fisika
# from . import math => di file __init__.py atau from .math import mtk
# from .mtk import kali,tambah di file __init__.py ke 2
# supaya dibawah dpt bekerja programny :

# import sains
# tmbh = sains.math.tambah(5,5)
# drifisika = sains.gaya(5,5)

# kali = sains.math.kali(5,7)
# print(tmbh)
# print(drifisika)
# print(kali)

#------------------------------------------
# __main__ => seperti int main(){} di c++
# print(__name__)

## contoh penggunaaan __main__
# import package # => package, nama modul buatan sendiri

# # deklarasi
# def tambah(a:int,b:int):
#     return a+b

# # fungsi utama
# if __name__ == "__main__":
#     angka1 = 5
#     angka2 = 10
#     hasil = tambah(angka1,angka2)
#     print(hasil)

#===============================================================================================================
# class Tes:
#     def __init__(self,nama,nim):
#         self.nama_a = nama
#         self.nim_a = nim


# def Tampil():
#     print(f"""
#     Nama Anda : {{}}
#     Nim Anda : {{}}
#     """.format(a.nama_a,a.nim_a))

# a = Tes("Tek kheng",20210801205)
# Tampil()

# a = 2

# if a == 1 :
#     print("if pertama = a")
# elif a == 2 :
#     print("if kedua == a")
# else : 
#     print("hehe")

# if a == 0:
#     print("0")
# elif a < 3 :
#     print("if ketiga = a")
# else :
#     print("default")

#==========================================================
# standard library python

# import
#------------------------------------------------------------
# import datetime as dataya 

# cara pakai dataya.datetime(tahun,bulan,lahir) 
# .strftime("%Y") mengubah menjadi format 2002
# .strftime("%y") mengubah menjadi format 02 -> untuk tahun
# .strftime("%m") mengubah menjadi format 02 -> untuk bulan
# .strftime("%d") mengubah menjadi format 17 -> untuk tgl

# .strftime("%H") mengubah menjadi jam
# .strftime("%M") mengubah menjadi menit
# .strftime("%S") mengubah menjadi detik

# .strftime("%x") mengubah menjadi format 17/5/02
# .strftime("%Y-%m-%d") mengubah menjadi format 2002-01-17

# import datetime as dt
# tgl_sekarang = dt.datetime.now()
# print(tgl_sekarang)
# print(tgl_sekarang.strftime("%H"))

# date_ini = dt.datetime(2002,1,17)
# wktu_ini = dt.time(5,4,6)
# print(date_ini.strftime("%x"))
# print(date_ini.strftime("%Y-%m-%d"))

# wktu = dt.datetime.now()
# print(wktu.strftime("%H-%M-%S"))
# print(date_ini.strftime("%A"))
# print(wktu_ini)
#------------------------------------------------------------
# import os
# os.system("cls") # => untuk windows
# os.system("clear") # => untuk linux

#--------------------------------------------------------
# import time
# timeJ = time.localtime()
# jam_t = time.strftime("%H",timeJ)
# menit_t = time.strftime("%M",timeJ)
# detik_t = time.strftime("%S",timeJ)

# atau
# waktu = time.strftime("%H %M %S",time.localtime())
# print(waktu)

#---------------------------------------------------------
# import string,random

# keyny = "".join(random.choice(string.ascii_uppercase) for i in range(5))
# print(keyny)

# data_siswa.update({keyny : dt_siswa})
#---------------------------------------------------------
# from copy import deepcopy

# list_2D_nested = [list_dt,list_dt2]
# list_deepcp = deepcopy(list_2D_nested)

#---------------------------------------------------------
# from collections import Counter

# # cara normal :
# data = ["a","t","h","y","a","b","b","t","a","b","h"]

# count = 0
# for i in data:
#     if i == "a":
#         count += 1
#     else:
#         continue
# print(f"data a berjumlah : {count}")

# # cara import :
# from collections import Counter
# hasil = Counter(data)
# print(hasil)
# print(f"data a berjumlah : {hasil.get('a')}")

#---------------------------------------------------------
# tkinter library standard
# GUI => Graphical User Interface
# sudo apt install python3-tk -y 
# hapus:
# sudo apt-get remove python3-tk 

# import tkinter as tk

# from tkinter import ttk

# root = tk.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# root.mainloop()

#======================================================================================
#### menggunakan package ####: 

# pip => untuk install packages
# pip => cek command

#$ sudo apt-get update
#$ sudo apt-get install python3-pip -y

# pip --version atau pip3 --version
# pip list

# upgrade versi terbaru pip :
# python3 -m pip install --upgrade pip

# install package :
# pip install nama_package
# pilih versi dengan pip install nama_package==versi

# cth :
# pip install numpy==1.21.0

# unistall :
# pip uninstall numpy 

# import numpy as np
# np.array(
#     [(5,2),(1,3)]
# )
# matrik = np.array([(1,2,3),(4,5,2)])
# hasil = matrik**2
# print(matrik)

# print(" ")
# arry = np.array([(1,True,"oi"),(4,"tes",2)])
# print(arry)

#----------------------------------------------------------------------------------------------
# pip install pygame
# import pygame

# pygame.init()

# # membuat display surface object
# window = pygame.display.set_mode((500,500))


# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             break
# pygame.quit()

#==========================================================================================================
#### Tutorial membaca dan write,etc file eksternal #### :
# mengakses file eksternal :
# "r" = read => lihat isi data
# "w" = write => overwrite,semuanya isiny ditimpa
# "a" = append => tambah isi yng sebelumny tidak di timpa
# "r+" = write read => lihat isi dan bisa timpa isi dengan write

# mode read:
# file = open("nama_file.txt",mode="r") #=> diakhir wajib harus close file dengan diakhiri file.close() 
# with open("nama_file.txt","r") as file :   #=> tidak perlu close karena sudah otomatis diclose 
#     print(f"isi file :  {file.read()}") #=> baca seluruh isi file

#     ## baca perbaris
#     print(file.readline()) # baca baris pertama
#     print(file.readline()) # baca baris selanjutny lgi/kedua
#     print(file.readline(),end="") # menghapus \n karena readline otomatis ada \n diujung baris jadi enter2x
    
#     print(file.readlines()) # baca semua baris sebagai list

#     # check status file bisa readable atau writable :
#     print(f"Status read file = {file.readable()}") #=> check status apakah bisa di read
#     print(f"Status write file = {file.writable()}") #=> check status apakah bisa di write

#     print(file.closed) #=> check status apakah file sudah di close

# # close file:
# file.close() #=> close file

# ## mode write(ubah isi dengan ditimpa keseluruhan isi dengan data baru dengan write)
# with open("nama_file.txt","w",encoding="utf-8") as file :
#     file.write("hello world")

## mode append(tambah isi) :
# with open("nama_file.txt","a",encoding="utf-8") as file :
#     file.write("\ntambah data baru")

# ## mode r+ => gabungan(lihat isi dan bisa write)
# with open("nama_file.txt","r+",encoding="utf-8") as file :
#     print(f"file sekarang: {file.read()}")
#     file.write("\ndiwrite dengan r+")
#     print(f"file setelah write: {file.read()}")

#--------------------------------------------------------------------------
## cara yg direkomendasikan => dengan with tidak perlu closed file lagi  :
# print(" Membaca file txt dengan with ".center(30,"="))
# # melihat data file eksternal
# with open("data.txt",mode="r") as file:
#     print(file.read())

#     print(file.readable())
#     print(file.writable())
#     print(file.closed)
# print(file.closed)

#=============================================================================================
# try and except => mirip seperti try and catch di javascript

# angka = int(input("masukkan angka : "))
# try :
#     hasil = 100/angka
# except :
#     print("angka tidak boleh 0")
#     hasil = 0
# print(f"hasil : {hasil}")

#-------------------------------------------------------------------
# def hitung():
#     bil1 = int(input("\nmasukkan bilangan 1 : "))
#     bil2 = int(input("masukkan bilangan 2 : "))
#     hasil = bil1 / bil2
#     return hasil

# while True:
#     try:
#         hasil = hitung()
#         print(hasil)
#         lnjt = input("lanjut ? y/n : ")
#         if lnjt == "n":
#             break
#         else : 
#             continue
#     except:
#         print("bilangan tidak boleh 0, silahkan input ulang")
#         hasil = 0

#-------------------------------------------------------------------
# while True:
#     try:
#         with open("latihan1.txt","r") as file :
#             print(file.read())
#         break
#     except:
#         with open("latihan1.txt","w", encoding="utf-8") as file :
#             file.write("woi hahah")
#             print("file latihan1.txt tidak ada, otomatis membuat file latihan1.txt")
#         break

#---------------------------------------------------------------------------------------
# contoh membuat exception sendiri :
# from numbers import Number

# def tambah(a,b):
#     if not isinstance(a,Number) or not isinstance(b,Number):
#         raise("input harus angka")
#     return a+b

# print(tambah(5,10))
# print(tambah("woi",10))



# def hitung():
#     bil1 = int(input("\nmasukkan bilangan 1 : "))
#     bil2 = int(input("masukkan bilangan 2 : "))
#     hasil = bil1 / bil2
#     return hasil

# while True:
#     try:
#         hasil = hitung()
#         print(hasil)
#         lnjt = input("lanjut ? y/n : ")
#         if lnjt == "n":
#             break
#         else : 
#             continue
#     except ZeroDivisionError as error_message:
#         print(error_message)




# genshin
import os
from random import randint,choice
if __name__ == "__main__":
    def header(pity,rate):
        print("Genshin Impact".center(30,"="))
        [print(f"{no+1:>13}.{i}") for no,i in enumerate(["Gacha","Exit"])]
        print(f"\nPity : {pity}")
        print(f"Kondisi Sekarang : {rate}")

    def main(): 
        sistem_operasi = os.name
        pity = 0
        rate = "Rate Of"
        items = "win","lose"
        while True:
            match sistem_operasi:
                case "posix" : os.system("clear")
                case "nt" : os.system("cls")
            header(pity,rate)
            rndm = randint(1,80)
            result = choice(items)
            try:
                pil = int(input("Pilih : "))
                
                if pil == 1:
                    pity += 1
                    if rndm == 15:
                        if result == "win":
                            print("Menang Banner Karakter b5")
                            pity = 0
                            rate = "Rate Of"
                        elif result == "lose":
                            print("dapat b5 yg tidak ada di banner!")
                            pity = 0
                            rate = "Rate On"
                        e = input("enter : ")
                    elif pity >=70:
                        if rndm >= 40:
                            if result == "win":
                                print("Menang Banner Karakter b5")
                                pity = 0
                                rate = "Rate Of"
                        elif result == "lose":
                            print("dapat b5 yg tidak ada di banner!")
                            pity = 0
                            rate = "Rate On"
                        e = input("enter : ")
                elif pil == 2:
                    break
            except:
                print("Format input harus angka!")
    main()
    print("Akhir Program")

