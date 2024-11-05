class TimProyek:
    def laporkan_kemajuan(self):
        print("Kemajuan proyek sedang dilaporkan.")

class TimPengembangan(TimProyek):
    def laporkan_kemajuan(self):
        print("Tim Pengembangan: Fitur baru telah selesai dan diuji.")

class TimPemasaran(TimProyek):
    def laporkan_kemajuan(self):
        print("Tim Pemasaran: Kampanye iklan telah diluncurkan.")

# Contoh penggunaan
tim_proyek = TimProyek()
tim_proyek.laporkan_kemajuan()  # Output: Kemajuan proyek sedang dilaporkan.

tim_pengembangan = TimPengembangan()
tim_pengembangan.laporkan_kemajuan()  # Output: Tim Pengembangan: Fitur baru telah selesai dan diuji.

tim_pemasaran = TimPemasaran()
tim_pemasaran.laporkan_kemajuan()  # Output: Tim Pemasaran: Kampanye iklan telah diluncurkan.

