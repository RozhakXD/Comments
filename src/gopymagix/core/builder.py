import os
import shutil
import sys
import time
from pathlib import Path
from typing import Optional

from .encoder import ScriptEncoder
from .compiler import GoCompiler

class GoPyMagixBuilder:
    """
    Mengorkestrasi proses build: enkripsi, pembuatan kode, dan kompilasi.
    Menghubungkan semua komponen modular dari pustaka.
    """
    def __init__(self, script_path: str, output_dir: str = "dist", output_name: Optional[str] = None, py_version: str = "3.13", keep_source: bool = False):
        self.script_path = Path(script_path)
        self.output_dir = Path(output_dir)
        self.output_name = output_name or self.script_path.stem
        self.py_version = py_version
        self.keep_source = keep_source

        if not self.script_path.is_file():
            raise FileNotFoundError(f"Berkas masukan tidak ditemukan di: '{self.script_path}'")
        
    def _get_go_template(self) -> str:
        """Membaca templat Go dari direktori resources."""
        try:
            template_path = Path(__file__).parent.parent / "resources" / "template.go"
            return template_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            raise RuntimeError("Berkas 'template.go' tidak ditemukan dalam direktori 'resources'.")
        
    def build(self):
        """Mengeksekusi seluruh alur kerja build dengan output log yang detail dan profesional."""
        total_start_time = time.time()
        
        def log(message):
            print(f"GoPyMagix: {message}")

        log("1.0.0 (c) 2025 Rozhak - https://github.com/RozhakDev/GoPyMagix")
        log(f"Memulai proses build untuk skrip '{self.script_path.resolve()}'.")
        log("Opsi build yang digunakan telah dikonfigurasi sebagai berikut:")
        log(f"  - Skrip Masukan         : '{self.script_path.resolve()}'")
        log(f"  - Direktori Output      : '{self.output_dir.resolve()}' (Lokasi penyimpanan biner akhir)")
        log(f"  - Nama Biner            : '{self.output_name}' (Nama file executable yang akan dihasilkan)")
        log(f"  - Versi Python Target   : '{self.py_version}' (Versi C-bindings yang akan ditautkan saat kompilasi)")
        log(f"  - Simpan Kode Sumber Go : {'Ya' if self.keep_source else 'Tidak'} (Kode sumber Go temporer akan {'disimpan' if self.keep_source else 'dihapus'} setelah build selesai)")
        log("----------------------------------------------------------------------")

        final_source_path = self.output_dir / f"{self.output_name}.go"

        try:
            log("Tahap 1/3: Enkripsi Skrip Python")
            start_time = time.time()
            encoded_code, original_size = ScriptEncoder.encode(self.script_path)
            duration = time.time() - start_time
            log(f"  - Membaca skrip sumber: '{self.script_path.name}' (ukuran: {original_size / 1024:.2f} KB).")
            log("  - Mengompresi dengan zlib dan mengenkode ke base64.")
            log(f"  - Enkripsi skrip berhasil diselesaikan dalam {duration:.2f} detik.")
            log("----------------------------------------------------------------------")

            log("Tahap 2/3: Pembuatan Kode Sumber Go")
            start_time = time.time()
            template = self._get_go_template()
            go_source = template.replace("{{PYTHON_CODE_B64}}", encoded_code)
            go_source = go_source.replace("{{PY_VERSION}}", self.py_version)
            duration = time.time() - start_time
            log(f"  - Memuat templat Go dari 'resources/template.go'.")
            log("  - Mengintegrasikan skrip terenkripsi ke dalam templat.")
            log(f"  - Mengonfigurasi C-bindings untuk Python {self.py_version}.")
            log(f"  - Pembuatan kode sumber Go berhasil diselesaikan dalam {duration:.2f} detik.")

            if self.keep_source:
                self.output_dir.mkdir(exist_ok=True)
                final_source_path.write_text(go_source, encoding='utf-8')
                log(f"  - Kode sumber Go disimpan secara permanen di: '{final_source_path.resolve()}'")
            log("----------------------------------------------------------------------")
            
            log("Tahap 3/3: Kompilasi Biner Go")
            log("  - Menjalankan 'go mod init gopymagix_build' di direktori temporer.")
            log("  - Menjalankan 'go mod tidy' untuk mengelola dependensi.")
            log(f"  - Mengompilasi 'main.go' menjadi biner '{self.output_name}' dengan CGO_ENABLED=1.")
            start_time = time.time()
            compiler = GoCompiler(go_source, self.output_name)
            temp_binary_path, _ = compiler.compile()
            duration = time.time() - start_time
            log(f"  - Kompilasi biner berhasil diselesaikan dalam {duration:.2f} detik.")
            log("----------------------------------------------------------------------")

            log("Proses Build Selesai")
            self.output_dir.mkdir(exist_ok=True)
            final_binary_path = self.output_dir / self.output_name
            shutil.move(str(temp_binary_path), final_binary_path)
            log(f"  - Memindahkan biner ke direktori output: '{final_binary_path.resolve()}'.")
            
            os.chmod(final_binary_path, 0o755)
            log("  - Mengatur izin file menjadi 755 (rwxr-xr-x).")

            binary_size = final_binary_path.stat().st_size
            total_duration = time.time() - total_start_time
            log(f"  - Ukuran biner akhir: {binary_size / 1024 / 1024:.2f} MB.")
            log(f"Build berhasil diselesaikan dalam {total_duration:.2f} detik.")
            log(f"Biner mandiri telah dibuat di: '{final_binary_path.resolve()}'")
        except (FileNotFoundError, RuntimeError) as e:
            log(f"ERROR: {e}")
            raise e