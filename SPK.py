print ("Selamat Datang di Program Pengiriman")
print ("-----------------------------------------------")
pengirim = input("Masukkan Nama Pengirim : ")
asal = input('Masukkan Kota Asal : ')
penerima = input("Masukkan Nama Penerima : ")
tujuan = input("Masukkan Kota Tujuan : ")

print ("===================================")

item1 = ['Paket','Dokumen']
item2 = ['Sangat Penting','Penting','Tidak Penting']
item3 = ['Cepat','Biasa']
item4 = ['Standar','Kayu']
item5 = ['Cukup','Baik','Sangat Baik']

print ("Jenis Kiriman Anda")
for i in range(0,len(item1)):
	print(i,item1[i])

jka = input('Masukkan Angka Yang dipilih : ')
ka = item1[int(jka)]

print ("===================================")

print ("Rekomendasi Harga")
for i in range(0,len(item2)):
	print(i,item2[i])

rh = input('Masukkan Angka Yang dipilih : ')
h = item2[int(rh)]

print ("===================================")

print ("Durasi Pengiriman")
for i in range(0,len(item3)):
	print(i,item3[i])

dp = input('Masukkan Angka Yang dipilih : ')
p = item3[int(dp)]

print ("===================================")

print ("Jenis Packing")
for i in range(0,len(item4)):
	print(i,item4[i])

jp = input('Masukkan Angka Yang dipilih : ')
pc = item4[int(jp)]

print ("===================================")

print ("Reputasi")
for i in range(0,len(item5)):
	print(i,item5[i])

rp = input('Masukkan Angka Yang dipilih : ')
r = item5[int(rp)]

print ("===================================")


import csv
dataku = open ('D:/database.csv','r')
data = csv.reader(dataku)
tabel = []
for i in data:
	tabel.append(i)

for i in range(0,len(tabel)):
	if tabel[i][0] == ka:
		if tabel[i][1] == h:
			if tabel[i][2] == p:
				if tabel[i][3] == pc:
					if tabel[i][4] == r:	
						print("Nama Pengirim: ",pengirim)
						print("Kota Asal : ",asal)
						print("Nama Penerima : ",penerima)
						print("Kota Tujuan : ",tujuan)
						print("Kiriman : ",ka)
						print("Jenis Packing : ",pc)
						print("Ekspedisi yang digunakan : ",tabel[i][5])