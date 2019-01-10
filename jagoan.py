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
	keberuntungan = 10

class pirAngkot(object):
	kekuatan = 100
	penyerangan = 70
	pertahanan = 100
	jangkauan = 150
	ilmuGaib = 0
	uang = 0
	name = "Sopir Angkot"
	keberuntungan = 10

class dukun(object):
	kekuatan = 100
	penyerangan = 60
	pertahanan = 100
	jangkauan = 50
	ilmuGaib = 140
	uang = 0
	name = "Mbah Dukun"
	keberuntungan = 10

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

def battleState():
	battleState = 100
	enemyNo = random.randint(0, 3)
	enemyList = [copet, preman, jambret, orgil]
	attackList = [character.kekuatan, character.ilmuGaib, character.jangkauan]
	print("Ada musuh datang ke pasar...")
	print("Ajegile, itu adalah seorang ", enemyList[enemyNo], "!!!" )
	print("Bersiaplah. Apa yang akan dilakukan sekarang \n")
	decision = int(input("1. Serang! \n2.Lihat isi tas. \n3. Kabur aja lah. Lagi males banget nih."))

	while decision > 3:
		print("isilah dengan angka 1,2 atau 3.")
		decision = int(input("1. Serang! \n2.Lihat isi tas. \n3. Kabur aja lah. Lagi males banget nih."))

	while decision == 1:
		if decision == 1:
			print("Kamu punya 3 pilihan menyerang")
			attack = int(input("1. Gagang pohon \n2. Ilmu Gaib \n3. Omelan"))
			x = attack - 1

			miss = random.randint(0,10) + character.keberuntungan

			if miss > 8:
				print("Serangannya luput! Musuh jago ngeles dot com")
				print("Musuh menyerang")
				print(enemyList[enemyNo], "melukai perasaan, harga diri dan tubuh anda")
				damage = round(enemyList[enemyNo].attack /character.pertahanan, 2)
				character.pertahanan = character.pertahanan - damage
				print("Kekuatan anda saat ini adalah tinggal ", character.pertahanan)
				if character.pertahanan < 10:
					print("Sebentar lagi anda mati, karena kekuatan tinggal sedikit. Perbanyaklah amal ibadah.")
				elif character.pertahanan < 1:
					print("Anda, jagoan kita meninggal dunia. Innalillahi.")
					print("GAME OVER")
					print("tekan keyboard control + C untuk keluar dari game ini dan merenungi makna hidup.")

			else:
				if attack == 1:
					damage = round(attackList[x] / enemyList[enemyNo].pertahanan, 2)
					print("Anda melawan balik dan membuat musuh menjadi berkurang pertahannnya sebanyak: ", damage)
					enemyList[enemyNo].kekuatan = enemyList[enemyNo].kekuatan - damage
					print("Kekuatan musuh berkurang. Sekarang tinggal: ", enemyList[enemyNo].kekuatan )
					if enemyList[enemyNo].pertahanan < 1:
						print(f"Musuh kita si {enemyList[enemyNo]} meninggal. Hamdalah. Walaupun ia musuh, jangan lupa disholati, sebab ia juga manusia seperti kita.")
						print("LANJUTKAN PETUALANGAN INI")
						enemyList[enemyNo].kekuatan = 100
						battleState = 0

						loot(enemyList[enemyNo])

					else:
						decision = int(input("1. Serang! \n2.Lihat isi tas. \n3. Kabur aja lah. Lagi males banget nih."))
						






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

