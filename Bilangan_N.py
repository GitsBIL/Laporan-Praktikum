# Program untuk menentukan bilangan terbesar dari N bilangan
print("Masukkan bilangan satu per satu.")
print("Masukkan 0 jika ingin berhenti.")

# Inisialisasi variabel max dengan nilai sangat kecil
max_value = float('-inf')  # -inf artinya negatif tak hingga, lebih kecil dari semua bilangan

while True:
    try:
        # Input bilangan dari pengguna
        bilangan = float(input("Masukkan bilangan: "))

        # Jika bilangan adalah 0, hentikan loop
        if bilangan == 0:
            break

        # Perbarui max jika bilangan lebih besar dari max_value saat ini
        if bilangan > max_value:
            max_value = bilangan

    except ValueError:
        print("Masukkan angka yang valid!")

# Periksa apakah ada bilangan yang dimasukkan selain 0
if max_value == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan selain 0.")
else:
    print(f"Bilangan terbesar adalah: {max_value}")

