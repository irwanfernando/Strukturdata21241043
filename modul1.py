
x = 10
y = -200
z = 0
print(type(x))   # <class 'int'>
print(type(y))   # <class 'int'>
print(type(z))   # <class 'int'>

# Operator penumlahan untuk tipe data integer
a1 = 5
a2 = -180

a3 = a1 + a2
print(a3)
print(type(a3))

a = 3.141592
b = -0.001
c = 1.0
d = float('inf')

print(a)
print(b)
print(c)
print(d)

print(type(a)) # <class 'float'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'float'>
print(type(d)) # <class 'float'>

print(a + c)
print(b ** a)
print(abs(a))

float = b * a
print(float)
print(type(float))

print(int(b * a))

a = 'Halo'
b = "python"
c = """Ini adalah string multi-baris"""
print(type(a))   # <class 'str'>
print(type(b))   # <class 'str'>
print(type(c))   # <class 'str'>

text = "python"
print(text[0])      #Output: p
print(text[-1])     #Output: n
print(text[0:3])    #Output: pyt
print(text[:4])     #Output: pyth
print(text[::2])    #Output: pto (loncat 2 karakter)

print('Hello ' + 'World')
print('Hi' * 3)
print('a' in 'data')
print(len('python'))

s = "python programing"
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.replace("python", "java"))
print(s.split())
print(s.find("gram"))

name = "Nando"
age  = 23
print(f"Halo, nama saya{name}, umur saya {age}")

print("Halo, nama saya {}, umur saya {}".format(name, age))

angka = [1, 2, 3, 4, 5,]
buah = ["apel", "jeruk", "mangga"]
campuran = [1, "dua", 3.0, True]
kosong = []

print(angka)
print(buah)
print(campuran)
print(kosong)

data = ["a", "b", "c", "d"]
print(data[0])
print(data[-1])
print(data[1:3])
print(data[:2])

data = [1, 2, 3, 4, 5]
data = data + [10, 20]
print(data)

list = [1, 2]
list = list * 3
print(list)

print(len(data))
print(len(list))

print(20 in data)
print(13 in list)

a = [3, 1, 4, 1, 5]
print(a)
a.append(9)
print(a)

a.insert(2, 7)
print(a)

a.remove(1)
print(a)

a.pop()
print(a)

a.sort()
print(a)

a.reverse()
print(a)
print(a.index(4))
print(a.count(1))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[1][2])

buah = ["apel", "jeruk", "mangga",]

for item in buah:
    print(item)

for i, item in enumerate(buah):
    print(f"{i}: {item}")

kuadrat = [x**2 for x in range(10)]
print(kuadrat)

genap = [x for x in range(10) if x % 2 == 0]
print(genap)

data_mahasiswa = []
jumlah = int(input("input jumlah mahasiswa: "))
for i in range(jumlah):
    print(f"/nmahasiswa ke-{i+1}:")
    nama = input("nama: ")
    nilai = list(map(int, input("mahasiswa 3 nilai dipisahkan spasi:").split()))
    rata2 = sum(nilai) / len(nilai)
    data_mahasiswa.append([nama, nilai, rata2])

print("/nData mahasiswa:")
print("Nama/tNilai/t/tRata-rata")
for siswa in data_mahasiswa:
    print(f"{siswa[0]}\t{siswa[1]}\t{siswa[2]:.2f}")

print("nMahasiswa Lulus (>= 75):")
for siswa in data_mahasiswa:
    if siswa[2] >= 75:
        print(f"{siswa[0]} - {siswa[2]:.2f}")


t = (1234, 'Helo world')
t1 = (1, 2, 3)
t2 = "a", "b", "c"
t3 = ()
t4 = (5,)

satu = ('Isi',)
dua = "ini adalah tuple?",

print(type(satu))
print(type(2))

satu = ('Isi')
dua = "ini adalah tuple"

print(type(satu))
print(type(dua))

nama = ('nando', 'fernando', 'irwan')
print(nama[1])

t = (1, 5, 10, 15)
t[0] = 0

angka = (10, 20, 30, 40)
print(angka[1:3])
print(angka[:2])
print(angka[2:])

print((1, 2) + (3, 4))
print(('A',) * 3)
data = (1, 2, 4, 5)
print(len(data))
print(3 in data)

t = (1, 2, (3, 4))
print(t[2][0])

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2)

print(tuple3)

t = ([1,2,3,4], True)
print (t)

web = 123, "PTI UNDIKMA", "https://fsttundikma.id"
id_web, nama, url = web
print(id_web)
print(nama)
print(url)

matkul_list = []
jumlah = int(input("Input jumlah mata kuliah: "))
for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)

print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)

('C5101', 'Algoritma', 3)
('C5102', 'Basis Data', 4)
('C5103', 'AI', 3)

total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")


nama_dict = {
    "key": "value"
}
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}
dict = {
    "nama"      : "Irwan Fernando",
    "NIDN"      : 21241043,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@Irwanfernando",
        "twiter"    : '_',
        "instagram" : '-'
    }
}

print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

print("NIDN Saya adalah %s" % dict.get('NIDN'))

nama_dict['kunci'] = 'Nilai_baru'
data['status'] = False

print(data['status'])

data.update({"sosmed" : {"twitter" : "@Irwanfernando"}})

print(data['sosmed']['twitter'])

del data['status']

print(data)

data.pop("sosmed")

print(data)

data.clear()

mahasiswa = {
    "name" : "Irwanfernando"
}
mahasiswa.update({
    "nidn" : "21241043"
})
print(mahasiswa)

for key in mahasiswa:
    print(key, mahasiswa[key])

for key, value in mahasiswa.items():
    print(f"{key}: {value}")

    data_mahasiswa = {
    "NIM001": {"nama": "Nando", "jurusan": "TI"},
    "NIM002": {"nama": "Irwan", "jurusan": "SI"}
}
data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan
    }
    
    print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}")
else:
    print("Mahasiswa tidak ditemukan.") 

    print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} → {info['nama']} ({info['jurusan']})")   