print("Kalkulator Luas Persegi Panjang")

panjang_str = input("Masukkan panjang: ")
lebar_str = input("Masukkan lebar: ")

# Proses konversi input string ke integer
panjang = int(panjang_str)
lebar = int(lebar_str)

# kalkukasi dilakukan setelah datanya menjadi angka
luas = panjang * lebar

print(f"Hasil perhitungan: {panjang} * {lebar} = {luas}")
