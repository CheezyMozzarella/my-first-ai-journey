print("--- Selamat datang di wahana roller coaster pythonator ---")
umur_user = int(input("Masukkan umur lo: "))
tinggi_user = int(input("Masukkan tinggi lo (cm): "))

#Cek syarat utama dulu
if umur_user >= 12 and tinggi_user >= 140:
    #kalo lolos syarat utama, cek syarat tambahan
    print("syarat utama sudah terpenuhi, pengecekan syarat tambahan...")
    sepatu_user = input("Apakah lo pake sepatu? (y/n): ")

    if sepatu_user == "y":
        print("Lengkap, lo boleh naik roller coaster!")
    else:
        #ini kalo syarat tambahan tidak terpenuhi
        print("Maaf, lo ga boleh naik roller coaster karena ga pake sepatu.")
else:
    #ini kalo syarat utama tidak terpenuhi
    print("Maaf, lo ga boleh naik roller coaster karena belum cukup umur atau tinggi badan lo kurang dari 140 cm.")

print("--- Terima kasih sudah bermain di wahana roller coaster pythonator ---")
