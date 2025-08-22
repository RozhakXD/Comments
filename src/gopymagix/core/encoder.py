import base64
import zlib
from pathlib import Path

class ScriptEncoder:
    """
    Bertanggung jawab untuk proses enkripsi berkas Python.
    Membaca berkas, mengompresi, dan mengenkripsi ke base64.
    """
    @staticmethod
    def encode(script_path: Path) -> tuple[str, int]:
        """
        Mengeksekusi alur kerja enkripsi: baca -> kompresi -> enkripsi.

        Args:
            script_path: Objek Path menuju berkas Python.

        Returns:
            Tuple berisi string base64 dari kode yang telah diproses dan ukuran file asli.
        
        Raises:
            FileNotFoundError: Jika berkas masukan tidak ditemukan.
            RuntimeError: Untuk kegagalan proses internal lainnya.
        """
        try:
            content = script_path.read_bytes()
            compressed = zlib.compress(content)
            encoded = base64.b64encode(compressed)
            return encoded.decode('utf-8'), len(content)
        except FileNotFoundError:
            raise
        except Exception as e:
            raise RuntimeError(f"Proses enkripsi gagal: {e}")