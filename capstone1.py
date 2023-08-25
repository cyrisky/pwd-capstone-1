Menu = [
    '1. Lihat Daftar Buku',
    '2. Tambah Buku',
    '3. Hapus Buku',
    '4. Mengubah Buku',
    '5. Cari Buku',
    '6. Pinjam Buku',
    '7. Lihat Buku yang Dipinjam',
    '8. Kembalikan Buku',
    '9. Exit'
]

Perpustakaan = [{
    'id': 1,
    'judul': 'How to Win Friends and Influence People in the Digital Age',
    'penulis': 'Dale Carnegie',
    'penerbit': 'Gramedia Pustaka Utama',
    'harga': 89000
}, {
    'id': 2,
    'judul': 'The Secret : Rahasia',
    'penulis': 'Rhonda Byrne',
    'penerbit': 'Gramedia Pustaka Utama',
    'harga': 110000
}, {
    'id': 3,
    'judul': 'Kecerdasan Emosional',
    'penulis': 'Daniel Goleman',
    'penerbit': 'Gramedia Pustaka Utama',
    'harga': 115000
}]

for book in Perpustakaan:
    book['dipinjam'] = False
    book['peminjam'] = None

### Fungsi Daftar Buku ###
def lihat_daftar_buku():
    print("\nDaftar Judul Buku:")
    for index, book in enumerate(Perpustakaan, 1):
        print(f"{index}. {book['judul']}")

    try:
        choice = int(input("\nPilih buku berdasarkan nomor untuk melihat detailnya: "))
        if 1 <= choice <= len(Perpustakaan):
            book = Perpustakaan[choice - 1]
            print(f"\nDetail Buku '{book['judul']}':")
            print(f"ID: {book['id']}")
            print(f"Judul: {book['judul']}")
            print(f"Penulis: {book['penulis']}")
            print(f"Penerbit: {book['penerbit']}")
            print(f"Harga: {book['harga']}")
        else:
            print("Nomor yang Anda pilih tidak valid.")
    except ValueError:
        print("Input salah. Silahkan masukkan nomor yang sesuai.")

### Fungsi Tambah Buku ###
def tambah_buku():
    id = len(Perpustakaan) + 1
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    penerbit = input("Masukkan nama penerbit: ")
    harga = int(input("Masukkan harga buku: "))

    print("\nData yang Anda masukkan:")
    print(f"ID: {id}")
    print(f"Judul: {judul}")
    print(f"Penulis: {penulis}")
    print(f"Penerbit: {penerbit}")
    print(f"Harga: {harga}")

    confirm = input("\nApakah Anda ingin menyimpan data ini? (y/n): ").lower()
    if confirm == 'y':
        Perpustakaan.append({
            'id': id,
            'judul': judul,
            'penulis': penulis,
            'penerbit': penerbit,
            'harga': harga
        })
        print("Buku berhasil ditambahkan!")
    else:
        print("Data buku tidak disimpan.")

### Fungsi Hapus Buku ###
def hapus_buku():
    id = int(input("Masukkan ID buku yang ingin dihapus: "))
    book_to_delete = None
    for book in Perpustakaan:
        if book['id'] == id:
            book_to_delete = book
            break

    if book_to_delete:
        print("\nDetail Buku yang akan dihapus:")
        print(f"ID: {book_to_delete['id']}")
        print(f"Judul: {book_to_delete['judul']}")
        print(f"Penulis: {book_to_delete['penulis']}")
        print(f"Penerbit: {book_to_delete['penerbit']}")
        print(f"Harga: {book_to_delete['harga']}")

        confirm = input("\nApakah Anda yakin ingin menghapus buku ini? (y/n): ").lower()
        if confirm == 'y':
            Perpustakaan.remove(book_to_delete)
            print("Buku berhasil dihapus!")
        else:
            print("Operasi penghapusan dibatalkan.")
    else:
        print("Buku dengan ID tersebut tidak ditemukan.")

### Fungsi Mengubah Buku ###
def mengubah_buku():
    id = int(input("Masukkan ID buku yang ingin diubah: "))
    book_to_update = None
    for book in Perpustakaan:
        if book['id'] == id:
            book_to_update = book
            break

    if book_to_update:
        print("\nDetail Buku saat ini:")
        print(f"ID: {book_to_update['id']}")
        print(f"Judul: {book_to_update['judul']}")
        print(f"Penulis: {book_to_update['penulis']}")
        print(f"Penerbit: {book_to_update['penerbit']}")
        print(f"Harga: {book_to_update['harga']}")

        judul = input("\nMasukkan judul buku baru: ")
        penulis = input("Masukkan nama penulis baru: ")
        penerbit = input("Masukkan nama penerbit baru: ")
        harga = int(input("Masukkan harga buku baru: "))

        print("\nDetail Buku yang baru:")
        print(f"ID: {id}")
        print(f"Judul: {judul}")
        print(f"Penulis: {penulis}")
        print(f"Penerbit: {penerbit}")
        print(f"Harga: {harga}")

        confirm = input("\nApakah Anda yakin ingin mengubah detail buku ini? (y/n): ").lower()
        if confirm == 'y':
            book_to_update['judul'] = judul
            book_to_update['penulis'] = penulis
            book_to_update['penerbit'] = penerbit
            book_to_update['harga'] = harga
            print("Buku berhasil diubah!")
        else:
            print("Perubahan dibatalkan.")
    else:
        print("Buku dengan ID tersebut tidak ditemukan.")

### Fungsi Cari Buku ###
def cari_buku():
    judul = input("Masukkan judul buku yang ingin dicari: ")
    for buku in Perpustakaan:
        if judul.lower() in buku['judul'].lower():
            print(f"ID: {buku['id']}, Judul: {buku['judul']}, Penulis: {buku['penulis']}, Penerbit: {buku['penerbit']}, Harga: {buku['harga']}")
            return
    print("Buku dengan judul tersebut tidak ditemukan.")

### Fungsi Pinjam Buku ###
def pinjam_buku():
    lihat_daftar_buku()
    try:
        id = int(input("\nMasukkan ID buku yang ingin dipinjam: "))
        for book in Perpustakaan:
            if book['id'] == id:
                if not book['dipinjam']:
                    nama_peminjam = input("Masukkan nama Anda: ")
                    book['dipinjam'] = True
                    book['peminjam'] = nama_peminjam
                    print(f"Buku '{book['judul']}' berhasil dipinjam oleh {nama_peminjam}!")
                else:
                    print(f"Buku '{book['judul']}' sudah dipinjam oleh {book['peminjam']}.")
                return
        print("Buku dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("Input salah. Silahkan masukkan ID buku yang valid.")

### Fungsi Lihat Buku Dipinjam ###
def lihat_buku_dipinjam():
    print("\nDaftar Buku yang Sedang Dipinjam:")
    found = False
    for book in Perpustakaan:
        if book['dipinjam']:
            found = True
            print(f"ID: {book['id']}, Judul: {book['judul']}, Peminjam: {book['peminjam']}")
    if not found:
        print("Tidak ada buku yang sedang dipinjam.")

### Fungsi Kembalikan Buku ###
def kembalikan_buku():
    lihat_buku_dipinjam()
    try:
        id = int(input("\nMasukkan ID buku yang ingin dikembalikan: "))
        for book in Perpustakaan:
            if book['id'] == id:
                if book['dipinjam']:
                    book['dipinjam'] = False
                    print(f"Buku '{book['judul']}' berhasil dikembalikan. Terima kasih, {book['peminjam']}!")
                    book['peminjam'] = None
                else:
                    print(f"Buku '{book['judul']}' saat ini tidak dipinjam.")
                return
        print("Buku dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("Input salah. Silahkan masukkan ID buku yang valid.")

### MENU ###
while True:
    print("\nMENU")
    for item in Menu:
        print(item)
    try:
        choice = int(input("\nPilih opsi (1-9): "))

        if choice == 1:
            lihat_daftar_buku()
        elif choice == 2:
            tambah_buku()
        elif choice == 3:
            hapus_buku()
        elif choice == 4:
            mengubah_buku()
        elif choice == 5:
            cari_buku()
        elif choice == 6:
            pinjam_buku()
        elif choice == 7:
            lihat_buku_dipinjam()
        elif choice == 8:
            kembalikan_buku()
        elif choice == 9:
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silahkan masukkan angka 1-9.")
    except ValueError:
        print("Input salah. Silahkan masukkan angka 1-9.")
