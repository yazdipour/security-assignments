import struct
import subprocess

uid = subprocess.check_output('id -ur', shell=True)
iuid = int(uid)
xuid = hex(iuid)
print xuid ##0x3e8
buid = struct.pack("I", iuid) #'\xe8\x03\x00\x00'
print buid
