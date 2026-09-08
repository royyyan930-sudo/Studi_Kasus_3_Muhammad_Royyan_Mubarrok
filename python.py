print ("---------Perpustakaan Buku-------")
buku_perpustakaan = ["b.inggris","B.indonesia","buku python","buku sejarah","buku pancasila"]
print(buku_perpustakaan)

pinjaman = []

for i in range(len(buku_perpustakaan)):
    print(i + 1,buku_perpustakaan[i])

while True:
    pilihan = input("Masukkan Judul Buku(Ketik Selesai untuk Berenti):")
    if pilihan == "selesai":
        break
    if pilihan in buku_perpustakaan:
        pinjaman.append(pilihan)
        print("buku berhasil dipinjam.")
    else:
        print("buku tidak tersedia")

print("------DAFTAR BUKU YANG DIPINJAM-------")

for buku in pinjaman:
    print(buku)

if len(pinjaman) > 0:
    hapus = input("masukkan judul buku yang mau dihapus:")
    if hapus in pinjaman:
        pinjaman.remove(hapus)
        print("buku berhasil dihapus")
    else:
        print("Buku tidak ada dalam daftar pinjaman")

print("------DAFTAR AKHIR BUKU YANG DIPINJAM------")

for buku in pinjaman:
    print(buku)