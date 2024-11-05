class Kendaraan:
    def berjalan(self):
        print("berjalan..")

class Mobil(Kendaraan):
    pass

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan()