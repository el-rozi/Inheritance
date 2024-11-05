# Pewarisan (Inheritance) Lanjutan 

## source : https://github.com/el-rozi

Dokumen ini menjelaskan konsep pewarisan dalam pemrograman berorientasi objek, dengan fokus pada penggunaan konstruktor dalam kelas turunan dan cara mengelola pewarisan dengan benar menggunakan Python.

### 1. Membuat Konstruktor pada Kelas Turunan

Konstruktor pada kelas turunan memiliki perilaku yang berbeda dibandingkan dengan konstruktor pada kelas induk. Ketika kelas turunan memiliki konstruktor sendiri, konstruktor tersebut akan menimpa konstruktor dari kelas induk, sehingga konstruktor kelas induk tidak akan dieksekusi.

#### Contoh:
Misalkan kita memiliki kelas `Orang`, dan kita membuat kelas turunan `Pelajar` dan `Pekerja`. Jika kita menambahkan konstruktor pada kelas `Pelajar` dan `Pekerja`, konstruktor dari kelas `Orang` tidak akan dipanggil.

### 2. Fungsi `super().__init__()` atau `KelasInduk.__init__()`

Menimpa konstruktor kelas induk dapat menghilangkan sebagian dari manfaat pewarisan. Solusinya adalah dengan memanggil konstruktor kelas induk secara eksplisit.

- **Menggunakan `super().__init__()`**: Memanggil fungsi ini tanpa perlu mendefinisikan ulang `self`.
- **Menggunakan `KelasInduk.__init__()`**: Memanggil fungsi ini dengan mengirimkan `self` secara manual.

#### Contoh:
- Gunakan `super().__init__()` untuk kelas `Pelajar`.
- Gunakan `KelasInduk.__init__()` untuk kelas `Pekerja`.

### 3. Menambahkan Properti Baru yang Tidak Ada pada Induk

Kelas turunan dapat memiliki atribut atau metode tambahan yang tidak ada pada kelas induk. Ini memungkinkan fleksibilitas dalam mendefinisikan perilaku khusus untuk kelas turunan.

#### Contoh:
- Tambahkan atribut `sekolah` untuk kelas `Pelajar`.
- Tambahkan atribut `tempat_kerja` untuk kelas `Pekerja`.


---

