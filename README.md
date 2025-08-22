# GoPyMagix: Tool Pengamanan Skrip Python 🚀

![GoPyMagix Banner](https://github.com/user-attachments/assets/37f77d03-eb8e-41cd-bba2-e5b3f236c8c2)
[MIT License](https://opensource.org/licenses/MIT) | [Python Downloads](https://www.python.org/downloads/) | [Go Downloads](https://golang.org/dl/)

**Sebuah tool canggih untuk menyematkan skrip Python ke dalam Go binaries, mengamankan skrip Python Anda dengan mengkompilasinya menjadi standalone Go binaries.**

## 🎯 Ringkasan

GoPyMagix adalah *tool* inovatif yang menjembatani Python dan Go dengan menyematkan skrip Python langsung ke dalam *Go binaries*. Pendekatan ini memberikan keamanan, portabilitas, dan kesederhanaan *deployment* yang lebih baik untuk aplikasi Python. Kode Python Anda dienkripsi, disematkan, dan dieksekusi di dalam *Go binary* yang telah dikompilasi, sehingga sulit untuk direkayasa balik sambil mempertahankan fungsionalitas penuh.

## ✨ Fitur

- **📊 *Logging* Terperinci**: Umpan balik proses *build* yang komprehensif dengan informasi waktu.
- **🔐 Enkripsi Skrip**: Mengenkripsi skrip Python secara otomatis menggunakan kompresi zlib dan *encoding* base64.
- **🔧 Integrasi Mulus**: Menyematkan kode Python terenkripsi ke dalam templat Go dengan *C-bindings*.
- **⚡ Kompilasi Cepat**: Proses *build* yang efisien dengan laporan kemajuan yang terperinci.
- **🎯 Lintas Platform**: Mendukung berbagai sistem operasi dan arsitektur.
- **📦 *Standalone Binaries***: Membuat *executable* mandiri tanpa dependensi eksternal.
- **🛠️ Konfigurasi Fleksibel**: Versi Python yang dapat disesuaikan, direktori *output*, dan opsi *build*.
- **🔍 Opsi Penyimpanan *Source***: Opsi untuk menyimpan *source code* Go yang dihasilkan untuk keperluan *debugging*.

## 📋 Prasyarat

Sebelum menggunakan GoPyMagix, pastikan Anda telah menginstal yang berikut:

- **Python 3.11+** - Diperlukan untuk menjalankan *build tool*.
- **Go 1.19+** - Diperlukan untuk mengkompilasi *binary* akhir.
- **C Compiler** - Diperlukan untuk *Python C-bindings* (GCC, Clang, atau MSVC).
- **Python Development Headers** - Diperlukan untuk menyematkan *interpreter* Python.

### Persyaratan Spesifik Sistem

#### Linux/Ubuntu

```bash
sudo apt-get update
sudo apt-get install python3-dev build-essential
```

#### macOS

```bash
xcode-select --install
brew install python@3.11
```

#### Windows

- Instal Visual Studio Build Tools atau Visual Studio Community.
- Pastikan Python diinstal dengan *development headers*.

## 🚀 Instalasi

1. **Clone repositori:**
   
   ```bash
   git clone https://github.com/RozhakDev/GoPyMagix.git
   cd GoPyMagix
   ```

2. **Verifikasi prasyarat:**
   
   ```bash
   python3 --version  # Harus 3.11+
   go version         # Harus 1.19+
   ```

3. **Buat skrip build dapat dieksekusi (Linux/macOS):**
   
   ```bash
   chmod +x scripts/build
   ```

## 🏃 Mulai Cepat

1. **Buat skrip Python sederhana:**
   
   ```python
   # hello.py
   def main():
       print("Halo dari GoPyMagix!")
       return "Sukses!"
   
   if __name__ == "__main__":
       main()
   ```

2. **Bangun *binary*:**
   
   ```bash
   python3 scripts/build hello.py
   ```

3. **Jalankan *binary* yang telah dikompilasi:**
   
   ```bash
   ./dist/hello
   ```

## 📖 Penggunaan

### Penggunaan Dasar

```bash
python3 scripts/build <script_path> [options]
```

### Opsi Baris Perintah

| Opsi            | Singkat | Deskripsi                                       | *Default*         |
|:--------------- |:------- |:----------------------------------------------- |:----------------- |
| `--output-dir`  | `-o`    | Direktori *output* untuk *binary* yang dibangun | `dist`            |
| `--name`        | `-n`    | Nama kustom untuk *binary output*               | Nama *file* skrip |
| `--py-version`  |         | Versi Python target untuk *C-bindings*          | `3.13`            |
| `--keep-source` |         | Pertahankan *source code* Go yang dihasilkan    | `false`           |

### Contoh

**Build dasar:**

```bash
python3 scripts/build examples/eternal_love.py
```

**Direktori dan nama *output* kustom:**

```bash
python3 scripts/build my_script.py -o build -n my_app
```

**Tentukan versi Python dan simpan *source***:

```bash
python3 scripts/build app.py --py-version 3.12 --keep-source
```

**Build dengan semua opsi:**

```bash
python3 scripts/build src/main.py \
  --output-dir release \
  --name production_app \
  --py-version 3.11 \
  --keep-source
```

## 📁 Struktur Proyek

```
GoPyMagix/
├── src/
│   └── gopymagix/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── builder.py      # Logika orkestrasi utama
│       │   ├── compiler.py     # Penanganan kompilasi Go
│       │   └── encoder.py      # Utilitas enkripsi skrip
│       └── resources/
│           └── template.go     # Template binary Go
├── scripts/
│   └── build                   # Skrip build CLI
├── examples/
│   └── ...                     # Contoh skrip Python
├── dist/                       # Direktori output (dibuat saat build)
├── README.md
├── LICENSE
└── .gitignore
```

## 🔧 Cara Kerja

GoPyMagix mengikuti proses *build* tiga tahap:

### Tahap 1: Enkripsi Skrip

- Membaca skrip Python masukan.
- Mengompresi kode menggunakan kompresi zlib.
- Meng-*encode* data terkompresi menggunakan *encoding* base64.
- Mengukur dan melaporkan ukuran *file* asli.

### Tahap 2: Pembuatan *Source Code* Go

- Memuat templat Go dari `resources/template.go`.
- Menyuntikkan kode Python terenkripsi ke dalam templat.
- Mengonfigurasi *C-bindings* spesifik versi Python.
- Menghasilkan *source code* Go yang lengkap.

### Tahap 3: Kompilasi *Binary*

- Mengkompilasi *source code* Go yang dihasilkan menggunakan *compiler* Go.
- Menautkan dengan pustaka C Python.
- Membuat *binary executable* yang mandiri.
- Menerapkan izin *file* yang benar dan memindahkannya ke direktori *output*.

## 💡 Contoh

Contoh-contoh yang relevan dapat ditemukan di dalam direktori `examples/`, seperti `eternal_love.py`, `eternal_rindu.py`, dan `silent_love.py`.

## ⚙️ Konfigurasi

### Kompatibilitas Versi Python

GoPyMagix mendukung beberapa versi Python melalui parameter `--py-version`:

- **Python 3.13** (*default*)
- **Python 3.12**
- **Python 3.11**

### Optimasi *Build*

Untuk *build* produksi, pertimbangkan praktik-praktik berikut:

1. **Gunakan versi Python spesifik** untuk memastikan konsistensi di seluruh lingkungan.
2. **Aktifkan penyimpanan *source*** selama pengembangan untuk *debugging*.
3. **Pilih nama *binary* yang bermakna** untuk manajemen *deployment* yang lebih baik.
4. **Atur direktori *output*** berdasarkan lingkungan (*dev*, *staging*, *prod*).

## 🤝 Kontribusi

Kami menyambut baik kontribusi untuk GoPyMagix! Berikut cara Anda dapat membantu:

### Pengaturan Pengembangan

1. ***Fork* dan *clone* repositori.**
2. **Buat *virtual environment*:**
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Di Windows: venv\Scripts\activate
   ```
3. **Instal dependensi pengembangan.**
4. **Buat perubahan Anda dan uji secara menyeluruh.**
5. **Kirim *pull request* dengan deskripsi yang jelas.**

### Gaya Kode

- Ikuti PEP 8 untuk kode Python.
- Gunakan nama variabel dan fungsi yang bermakna.
- Tambahkan *docstrings* untuk semua fungsi dan kelas publik.
- Sertakan *type hints* jika sesuai.

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat *file* [LICENSE](LICENSE) untuk detailnya.