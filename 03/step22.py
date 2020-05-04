import struct
import subprocess

uid = subprocess.check_output('id -ur', shell=True)
iuid = int(uid)
xuid = hex(iuid)
print xuid
buid = struct.pack("I", iuid) #'\xe8\x03\x00\x00'
print buid
