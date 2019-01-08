# This is a game about hero and the monster

import random

# Hero class
class satpamPasar(object):
	kekuatan = 150
	penyerangan = 100
	pertahanan = 100
	jangkauan = 70
	ilmuGaib = 0
	uang = 0
	name = "Satpam Pasar"

class pirAngkot(object):
	kekuatan = 100
	penyerangan = 70
	pertahanan = 100
	jangkauan = 150
	ilmuGaib = 0
	uang = 0
	name = "Sopir Angkot"

class dukun(object):
	kekuatan = 100
	penyerangan = 60
	pertahanan = 100
	jangkauan = 50
	ilmuGaib = 140
	uang = 0
	name = "Mbah Dukun"

# class bandit
class copet(object):
	intro = "Loh dompet saya dimana?"
	kekuatan = 30
	penyerangan = 2
	pertahanan = 2
	kelangkaan = 0

class preman(object):
	intro = "Ape lo liatliat!"
	kekuatan = 50
	penyerangan = 5
	pertahanan = 10
	kelangkaan = 1

class jambret(object):
	intro = "Ada RX King berwarna hitam."
	kekuatan = 60
	penyerangan = 6
	pertahanan = 12
	kelangkaan = 2

class orgil(object):
	intro = "Tolong ada orang gila ga pake celana..."
	kekuatan = 70
	penyerangan = 10
	pertahanan = 15
	kelangkaan = 3

# inventory area
def inventoryWipe():
	file = open("inventory.txt", "w")
	file.close()

def inventoryShow():
	global contents
	print("Kamu memiliki benda ini dalam inventori : ")
	file.open("inventory.txt", "r")
	contents = file.read()
	contents = contents.split(",")
	print(contents)
	
	length = len(contents)-1
	for i in range(length):
		print(contents[i])

def lootCheck(lootX):
	file = open("inventory.txt", "r")
	contents = file.read()
	contents = contents.split(",")
	if lootX in contents:
		print("Sudah punya. Tidak bisa ambil lagi.")
	else:
		inventory(lootX)

def inventory(lootX):
	file = open("inventory.txt", "a")
	file.write(str(lootX + ","))
	file.close()

def inventoryDelete(decisionX):
	file = open("inventory.txt", "r")
	contents = file.read()
	contents = contents.split()
	file.close()
	print(contents)
	if decisionX in contents:
		i = contents.index(decisionX)
		del contents[i]
		print(contents)
		contents = contents[:-1]
		print(contents)

		file = open("inventory.txt", "w")
		for x in range (0, len(contents)):
			print(contents[x])
			file.write(contents[x] + ",")
		file.close()

def loot(enemyList, enemyNo):
	file = open("loot.txt", "r")
	lootTableCommon = file.readline()
	lootTableUnCommon = file.readline()
	lootTableRare = file.readline()
	lootTableUltraRare = file.readline()

	lootTableCommon = lootTableCommon.split(",")
	lootTableUnCommon = lootTableCommon.split(",")
	lootTableRare = lootTableCommon.split(",")
	lootTableUltraRare = lootTableCommon.split(",")

	lootTableCommon = lootTableCommon[:-1]
	lootTableUnCommon = lootTableCommon[:-1]
	lootTableRare = lootTableCommon[:-1]
	lootTableUltraRare = lootTableCommon[:-1]

	global lootX

	if enemyList(enemyNo).rarity == 0:
		length = len(lootTableCommon)-1
		lootX = lootTableCommon[random.randint(0, length)]

	elif enemyList(enemyNo).rarity == 1:
		length = len(lootTableCommon)-1
		lootX = lootTableCommon[random.randint(0, length)]

	elif enemyList(enemyNo).rarity == 2:
		length = len(lootTableCommon)-1
		lootX = lootTableCommon[random.randint(0, length)]

	elif enemyList(enemyNo).rarity == 3:
		length = len(lootTableCommon)-1
		lootX = lootTableCommon[random.randint(0, length)]

	else:
		length = len(lootTableCommon)-1
		lootX = lootTableCommon[random.randint(0, length)]
	
	lootX = str(lootX)
	print("Musuh menjatuhkan... ", lootX)
	lootCheck(lootX)

inventoryWipe()
print("\n \n \nKamu harus menjaga keamanan pasar dari serangan monster!\n \n \n")
print("Tapi sebelumnya, siapa kah kamu? (isi dengan nomor pilihan) ")

choice = int(input("1. Satpam Pasar \n2. Sopir Angkot \n3 Mbah Dukun. \nSaya pilih nomor... "))

nama = str(input("Siapa nama kamu? "))

if choice == 1:
	character = (satpamPasar)
	print("Pilihan yang baik. Anda sekarang adalah seorang " + character.name + " " + nama)

elif choice == 2:
	character = (pirAngkot)
	print("Pilihan yang baik. Anda sekarang adalah seorang " + character.name + " " + nama)

elif choice == 3:
	character = (dukun)
	print("Pilihan yang baik. Anda sekarang adalah seorang " + character.name + " " + nama)

else:
	print("Salah isi euy. Isi dengan nomor pilihan, 1, 2 atau 3. Yang pertama seorang Satpam Pasar, kedua adalah Sopir Angkot, yang terakhir, Mbah Dukun. Coba sekarang pilih lagi yang benar.")
	choice = int(input("1. Satpam Pasar \n2. Sopir Angkot \n3 Mbah Dukun. \nSaya pilih nomor... "))

