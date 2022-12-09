#==================================================================================================
# object oriented programming python:
# class hero:
#     pass


# hero1 = hero()
# hero1.name = "Yunia"
# hero1.hp = 1000

# hero2 = hero()
# hero2.name = "Popia"
# hero2.hp = 700

# print(hero1.__dict__)
# print(hero1.name)
# print(hero2.__dict__)
# print(hero2.name)

#==================================================================================================
# class with constructor __init__()
# class tes:
#     def __init__(self,name):
#         print("function __init__ otomatis Dieksekusi ketika program dijalankan")
#         print(f"Hallo {name}")

# mesin = tes("hevon")


# class hero:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp

# hero1 = hero("yuki",150)
# hero2 = hero("miki",120)

# print(hero1.__dict__)
# print(f"{hero1.name},HP : {hero1.hp}")
# print(f"{hero2.name},HP : {hero2.hp}")

# ======

#+================================================
# class hero:
#     # class variabel
#     jumlah_hero = 0

#     def __init__(self,input_name,input_health,input_power,input_armor):
#         # instance variabel
#         self.nama = input_name
#         self.health = input_health
#         self.power = input_power
#         self.armor = input_armor
#         hero.jumlah_hero += 1

#     # method :
#     def who(self):
#         print(f"namaku adalah {self.nama}")

#     def heal(self,heal):
#         self.health += heal
    
#     def getArmor(self):
#         return self.armor

# hero1 = hero("andi",800,79,56)
# hero2 = hero("Pupy",600,43,200)
# hero3 = hero("nika",590,90,105)

# hero1.who()
# hero1.heal(10)
# print(hero1.__dict__)

# print(hero1.getArmor())

# print(hero2.__dict__)
# print(hero3.__dict__)
# print(hero.jumlah_hero)    


#================================================
   # if hero.nama = "Yuki":
        #     hero1.hp -= (self.atk - self.armor)
        #     print(f"anda menyerang hero1, hp hero1={hero1.hp} menjadi hp={hero1.hp}")
            
        # elif "hero2" in hero:
        #     hero2.hp -= (self.atk - self.armor)
        #     print(f"anda menyerang hero2, hp hero2={hero2.hp} menjadi hp={hero2.hp}")


# class Hero:
#     def __init__(self,nama,hp,atk,armor):
#         self.nama = nama
#         self.hp = hp    
#         self.atk = atk
#         self.armor = armor
    
#     def attack(self, target):
#         print(f"{target.nama} - {target.hp}")
#         target.hp -= (self.atk / target.armor)
#         print(f"Player {self.nama} menyerang {target.nama}, hp menjadi {target.hp}")
        
#         target.defense(self.atk)

#     def defense(self,power):
#         print(f"{self.nama} terserang, {self.nama} menerima damage {power/self.armor}")
#         print(f"darah tersisa {self.hp}")

#     def recovery(self):
#         self.hp += 100

# player = Hero("Yuki",1200,15,5)
# enemy = Hero("MaguKen",1000,20,5)

# player.attack(enemy)
# print("")
# enemy.attack(player)


# =====================================================================
class Hero:
    __privateJumlah = 0
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

        self.__private = "private"

        self._protected = "protected"

t = Hero("kuki",17)

# print(Hero.__privateJumlah)
# print(t.__private)
t._protected = "woi"
print(t._protected)

print(t.__dict__)
print(t.__private)
# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()

# window.configure(bg="black")
# window.geometry("450x500")
# window.resizable(False,False)

# frm = ttk.Frame(window,padding=5)
# frm.pack(padx=50,fil="x",expand=True)

# text1 = ttk.Label(frm,text="ini text1")
# text1.pack(padx=10,fil="x",expand=True)

# window.mainloop()