class Karyawan:
    def hitung_gaji(self, jam_kerja, tarif_per_jam):
        return jam_kerja * tarif_per_jam

class KaryawanTetap(Karyawan):
    def hitung_gaji(self, jam_kerja, tarif_per_jam):
        gaji = super().hitung_gaji(jam_kerja, tarif_per_jam)
        tunjangan = 100000  # Tunjangan tetap
        return gaji + tunjangan

# Contoh penggunaan
karyawan = Karyawan()
print("Gaji Karyawan: ", karyawan.hitung_gaji(40, 15000))  # Output: 600000

karyawan_tetap = KaryawanTetap()
print("Gaji Karyawan Tetap: ", karyawan_tetap.hitung_gaji(40, 15000))  # Output: 700000

