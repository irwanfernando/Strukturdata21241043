# membuat dictionary
dict = {
    "nama"      : "Irwan Fernando",
    "NIDN"      : 62708078505,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@Nando",
        "twiter"    : '_',
        "instagram" : '-'
    }
    
}

print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])


print("NIDN Saya adalah %s" % dict.get('NIDN'))


dict['status'] = False
print(dict['status'])

