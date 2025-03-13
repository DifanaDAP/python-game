import random

class TebakAngka:
    # inisiasi game dengan angka rahasia yang dipilih secara acak dantara 1 - 100
    def __init__(self):
        self.angka_rahasia = random.randint(1, 100)
        self.tebakan = None
    
    def mulai(self):
        # menampilkan pesan selamat datang pada pemain
        print("Selamat datang di game tebak angka!")

        # Loop utama permainan, berjalan sampai pemain menebak angka dengan benar
        while self.tebakan != self.angka_rahasia:
            try:
                #meminta input dari pemain dalam interger
                self.tebakan = int(input("Tebakan angka antara 1-100 : "))

                # membeikan petunjutk apakah tebakan terlalu rendah atau terlalu tinggi
                if self.tebakan < self.angka_rahasia:
                    print("Telalu rendah! Coba lagi")
                elif self.tebakan > self.angka_rahasia:
                    print("Terlalu tinggi! coba lagi")
                else:
                    # tebakan benar dan ada pesan sukses dan keluar dari loop
                    print("Selamat! anda berhasil menebak angka")
            except ValueError:
                # menangani kesalahan jika bukan angka yang di input
                print("masukan angka yang valid")

# Menjalankan Game
if __name__ == "__main__":
    game = TebakAngka()
    game.mulai()