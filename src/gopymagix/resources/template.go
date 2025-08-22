package main

/*
// Menggunakan 'python3' sebagai target pkg-config untuk kompatibilitas luas.
#cgo pkg-config: python3

// LDFLAGS secara eksplisit menautkan pustaka Python versi spesifik untuk build yang andal.
#cgo LDFLAGS: -lpython{{PY_VERSION}}

#include <Python.h>
*/
import "C"
import (
	"bytes"
	"compress/zlib"
	"encoding/base64"
	"io"
	"log"
	"unsafe"
)

const codeB64 = `{{PYTHON_CODE_B64}}`

func decodeAndDecompress(encoded string) []byte {
	decoded, err := base64.StdEncoding.DecodeString(encoded)
	if err != nil {
		log.Fatalf("FATAL: Proses dekode base64 gagal: %v", err)
	}

	b := bytes.NewReader(decoded)
	r, err := zlib.NewReader(b)
	if err != nil {
		log.Fatalf("FATAL: Inisialisasi zlib reader gagal: %v", err)
	}
	defer r.Close()

	decompressed, err := io.ReadAll(r)
	if err != nil {
		log.Fatalf("FATAL: Proses dekompresi zlib gagal: %v", err)
	}
	return decompressed
}

func main() {
	pySrc := decodeAndDecompress(codeB64)

	C.Py_Initialize()
	if C.Py_IsInitialized() == 0 {
		log.Fatal("FATAL: Inisialisasi interpreter Python gagal.")
	}

	cStr := C.CString(string(pySrc))
	defer C.free(unsafe.Pointer(cStr))

	if C.PyRun_SimpleString(cStr) != 0 {
		log.Fatal("FATAL: Eksekusi skrip Python gagal.")
	}

	C.Py_Finalize()
}