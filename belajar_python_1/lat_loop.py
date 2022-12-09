# a = 5
# b = 3

# count = 9
# while a > b:
#     print("*"*count)
#     count -= 1
#     if count == 0:
#         break
#     elif count % 3:
#         count -= 1
#         continue
#---------------------------------------------------------------------------------------------------------------
# count = 10
# for i in range(1,11):
#     print("*"*count)
#     count -= 1

#     if count == 0:
#         count += 1
#         for i in range(1,11):
#             count += 1
#             print("*"*count)
#---------------------------------------------------------------------------------------------------------------
# For
# count = 1
# for i in range(11):
#     print("*"*count)
#     count +=1

#     if count > 10:
#         for i in range(11):
#             print("*"*count)
#             count -= 1
#---------------------------------------------------------------------------------------------------------------
# while :
# count = 1
# while True:
#     if count >=1 and count < 10:
#         print("*"*count)
#         count += 1

#     elif count == 10:
#         count -= 1
#         while True:
#             count -= 1
#             print("*"*count)
#             if count < 1:
#                 break

#-----------------------------------------------------------------------------------------------------------
# count = 1
# while count >=1 and count < 10 :
#     print("*"*count)
#     count += 1

#     if count == 10:
#         count -= 1
#         while True:
#             count -= 1
#             print("*"*count)
#             if count < 1:
#                 break
#------------------------------------------------------------------------------------------------------------        

# angka = [0,1,2,3,4,5]
# for i in angka:
#     print(f"{i+1}.{i}")

# str_tes = "Tekkheng"
# count = 1
# for i in str_tes:
#     print(i*count)
#     count +=1
#---------------------------------------------------------------------------------------------------------------
# while no infinity
# angka_pass = 0
# while angka_pass <= 10:
#     angka_pass +=1
#     if angka_pass == 3:
#         print("skip")
#         continue

#     print(f"{angka_pass}.jumlah")
# print("finish")

#---------------------------------------------------------------------------------------------------------------
# count = 1
# while count >= 1 and count <= 10:
#     print(f"+"*count)
#     count +=1

#     if count > 10:
#         for i in range(11):
#             print("+"*count)
#             count -= 1
#     elif count < 1:
#         break
 

# count = 1
# while count >= 1 and count <= 10:
#     print(f"+"*count)
#     count +=1

#     if count >= 11 :
#         while True:
#             print("+"*count)
#             count -= 1
#             if count < 1:
#                 break



# count = 1
# while count >=1 and count < 10 :
#     print("*"*count)
#     count += 1

#     if count == 10:
#         count -= 1
#         while True:
#             count -= 1
#             print("*"*count)
#             if count < 1:
#                 break



# count = 1
# while count >= 1 and count < 10:
#     print(f"+"*count)
#     count +=1

#     if count == 10 :
#         while True:
#             print("+"*count)
#             count -= 1
#             if count < 1:
#                 break
#---------------------------------------------------------------------------------------------
count = 10
while count <= 10:
    print("+"*count)
    count -= 1

    # if count <= 1:
    #     break

    if count <=5 :
        count +=2
        while count > 5 and count <= 9:
            count += 1
            print("+"*count)

            if count % 3:
                count +=1
                continue

            elif count > 9:
                break

    elif count %4:
        count -=1
        continue
#---------------------------------------------------------------------------------------------
# count = 16
# while count <= 16:
#     print("+"*count)
#     count -= 1

#     # if count <= 1:
#     #     break

#     if count <=5 :
#         count +=2
#         while count > 5 and count <= 16:
#             count += 1
#             print("+"*count)

#             if count % 9:
#                 count +=1
#                 continue

#             elif count > 16:
#                 break

#     elif count %4:
#         count -=1
#         continue
#---------------------------------------------------------------------------------------------
# count = 1
# space = int(10/2)
# while True :
#     if (count % 2) :
#         print(" "*space,"+"*count)
#         space -=1
#         count +=1
#     else:
#         count+=1
#         continue
#     if count > 9 :
#         break
#---------------------------------------------------------------------------------------------

# count =1
# n = 10
# spasi = int(n/2)

# for i in range(n):
#     if (count % 2):
#         print(" "*spasi,"+"*count)
#         count +=1
#         spasi -= 1
#     else:
#         count +=1
#         continue
#---------------------------------------------------------------------------------------------    

# class dataAkheng :
#     def __init__(self,nim,nama,jurusan,umur,agama,jns_klmn):
#         self.nim = nim
#         self.nama = nama
#         self.jrsn = jurusan
#         self.umur = umur
#         self.agama = agama
#         self.gender = jns_klmn

# def getter_dt():
#     print("BIODATA".center(30,"="))
#     print("""
#     Nim : {}
#     Nama : {}
#     Jurusan : {}
#     Umur : {}
#     Agama : {}
#     Jenis Kelamin : {}
#     """.format(dt.nim,dt.nama,dt.jrsn,dt.umur,dt.agama,dt.gender))
#     print("=".center(30,"="))
    
# dt = dataAkheng(20210801205,"Tek kheng","Teknik Informatika",20,"Budha","Laki-laki")
# getter_dt()
#---------------------------------------------------------------------------------------------

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


