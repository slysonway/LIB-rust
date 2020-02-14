from ctypes import cdll
lib = cdll.LoadLibrary("../ppm/target/debug/libppm.dylib")

print(lib.dummy())

print(lib.times(2, 5))

# //print(lib.readPPM('a'))


