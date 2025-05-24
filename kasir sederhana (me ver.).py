barang = {
    "KEMEJA": 50000,
    "KAOS": 30000,
    "CELANA JEANS": 60000,
    "JAKET": 100000
}



def pembayaran():
    seluruh_total = 0
    while True:
        while True:
            print("\nStok barang yang tersedia:")
            for item in barang:
                print(f"{item}: Rp.{barang[item]}")
            
            input_pilihan = input("Masukan Nama Barang Yang Dibeli: ").upper()

            if input_pilihan.lower() == "n":
                break

            if input_pilihan in barang:
                print(f"Anda memilih {input_pilihan}")
                jumlah_beli = int(input("Masukan Jumlah Yang Dibeli: "))
                total_harga = jumlah_beli * barang[input_pilihan]
                print(f"Total harga: Rp.{total_harga}")

                seluruh_total += total_harga

                lanjut_belanja = input("Apakah ingin melanjutkan belanja? (y/n) ").lower()
                if lanjut_belanja == "n":
                    break

            else:
                print("Barang tidak tersedia")

        print(f"\nTotal seluruh belanjaan anda: Rp.{seluruh_total} \n")
    
        lanjut_pembayaran = input("Lanjut opsi pembayaran(y)/ Kembali ke menu opsi(n): ")
        if lanjut_pembayaran == "n":
            break

def stok_barang():
    while True:
        print("\nSilahkan tulis dengan mencantumkan nama dan harga barang:")
        input_nama_stok = input("Masukan nama barang: ").upper()
        input_harga_stok = int(input("Masukan nama barang: "))
        barang[input_nama_stok]=input_harga_stok

        lanjut = input("Lanjut memasukan stok(y)/ Kembali ke opsi menu(n): ")
        if lanjut == "n":
            print("Barang berhasil ditambahkan ke dalam stok")
            break


while True:
    print("\n*************************************")
    print("""Pilih opsi menu:
          1. Memasukan stok barang
          2. Melakukan pembayaran""")
    print("\n*************************************")
    
    input_opsi = int(input("masukan angka pilihan opsi: "))

    if input_opsi == 1:
        stok_barang()
    
    elif input_opsi == 2:
        pembayaran()
    
    else:
        print("Pilihan tidak tersedia")

