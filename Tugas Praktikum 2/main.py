a = int(input("Masukan bilangan ke-1 :"))
b = int(input("Masukan bilangan ke-2 :"))
c = int(input("Masukan bilangan ke-3 :"))

# Menggunakan statement ifvuntuk menentukan bilangan terbesar
if a > b and a > c:
    print("nilai a terbesar")
elif b > a and b > c:
    print("nilai b terbesar")
else:
    print("nilai c terbesar")           