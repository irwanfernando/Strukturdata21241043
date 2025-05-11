a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>

# indexing dan slicing 
text = "IRWAN"
print(text[0])     # Output: I
print(text[-1])    # Output: W
print(text[0:3])   # Output: IRW
print(text[:4])    # Output: IRWA
print(text[::2])   # Output: IWA (loncat 2 karakter)

# Operasi penggabungan string
print('Hello ' + 'IRWAN')

# Operasi pengulangan string
print('HOHO' * 3)

# Operasi Pengecekan string
print('a' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('IRWAN'))

s = "irwan programming"
print(s.upper())       # 'IRWAN PROGRAMMING'
print(s.capitalize())  # 'IRWAN programming'
print(s.title())       # 'IRWAN Programming'
print(s.replace("irwan", "java"))  # 'java programming'
print(s.split())       # ['IRWAN', 'programming']
print(s.find("gram"))  # 10 

# F-String
# String format menggunakan F-String
name = "Irwan"
age = 23
print(f"Halo, nama saya {name}, umur saya {age}")

# Format Method
# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))

