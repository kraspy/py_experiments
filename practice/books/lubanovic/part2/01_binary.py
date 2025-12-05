from pathlib import Path
import re
import binascii
import struct

BASE_DIR = Path(__file__).parent


# 12.1
import unicodedata

mystery = '\U0001f4a9'
print(mystery, unicodedata.name(mystery))

# 12.2
pop_types = mystery.encode('utf-8')
print(pop_types)

# 12.3
print(pop_types.decode('utf-8'))

# 12.4
with open(BASE_DIR / 'mammoth.txt', 'r') as f:
    text = f.read()

print(text[:50])

# 12.5
print(re.findall(r'\bs.*?\b', text))

# 12.6
print(re.findall(r'\bc\w{3}\b', text))

# 12.7
print(re.findall(r'\b\w+?r\b', text))

# 12.8
print(re.findall(r'\b.\w*[aeiou]{3}\w*\b', text))

# 12.9
hex_str = (
    '47494638396101000100800000000000ffffff21f9'
    '0401000000002c000000000100010000020144003b'
)
gif = binascii.unhexlify(hex_str)

print(gif)

# 12.10
print('Correct GIF' if gif.startswith(b'GIF89a') else 'Incorrect GIF')

# 12.11
gif_width, gif_height = struct.unpack('<HH', gif[6:10])
print(gif_width, gif_height)
