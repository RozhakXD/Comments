import shutil
import subprocess
import os
import tempfile
from pathlib import Path

class GoCompiler:
    """
    Mengelola kompilasi kode sumber Go menjadi berkas biner.
    Menggunakan direktori temporer untuk memastikan proses build yang bersih.
    """
    def __init__(self, go_source: str, output_name: str):
        self.go_source = go_source
        self.output_name = output_name

    def compile(self) -> tuple[Path, Path]:
        """
        Menjalankan proses kompilasi dalam direktori temporer.

        Returns:
            Tuple berisi objek Path menuju biner dan kode sumber Go yang digunakan.
        
        Raises:
            RuntimeError: Jika kompilasi gagal.
        """
        with tempfile.TemporaryDirectory() as temp_dir_str:
            temp_dir = Path(temp_dir_str)
            go_main_path = temp_dir / "main.go"
            go_main_path.write_text(self.go_source, encoding='utf-8')

            for cmd in [["go", "mod", "init", "gopymagix_build"], ["go", "mod", "tidy"]]:
                self._run_command(cmd, temp_dir)

            binary_path = temp_dir / self.output_name
            build_command = ["go", "build", "-o", str(binary_path), "-ldflags=-s -w", "."]

            self._run_command(build_command, temp_dir, cgo_enabled=True)

            final_binary_path = self._move_to_safe_temp(binary_path)
            final_source_path = self._move_to_safe_temp(go_main_path)

            return final_binary_path, final_source_path

    @staticmethod
    def _run_command(command: list[str], cwd: Path, cgo_enabled: bool = False):
        """Fungsi pembantu untuk menjalankan perintah eksternal."""
        env = os.environ.copy()
        if cgo_enabled:
            env["CGO_ENABLED"] = "1"

        try:
            subprocess.run(
                command, cwd=str(cwd), env=env, check=True, capture_output=True, text=True
            )
        except subprocess.CalledProcessError as e:
            error_message = (
                f"Perintah kompilasi `{' '.join(command)}` gagal. "
                f"Pastikan Go, C compiler (gcc/clang), pkg-config, dan pustaka python-dev terinstal dengan benar.\n"
                f"--> Pesan dari kompiler: {e.stderr.strip()}"
            )
            raise RuntimeError(error_message)
        
    @staticmethod
    def _move_to_safe_temp(source_path: Path) -> Path:
        """Memindahkan berkas ke lokasi temporer yang persisten."""
        with tempfile.NamedTemporaryFile(delete=False, prefix=f"{source_path.name}-") as f:
            safe_path = Path(f.name)
        shutil.move(str(source_path), safe_path)
        return safe_path