# Program Menjumlahkan Nilai awal
# Oleh :  Tatsbita Thifalia
#         20051397027
#         2020A D4 Manajemen Informatika

print("angka = 1234")

def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

numbers = [1, 2, 3, 4]
print("jumlah dari angka = " + str(sum(numbers)))