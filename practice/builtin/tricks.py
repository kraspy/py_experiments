print(all(x > 0 for x in [0, 1, 2]))
print(any(x > 0 for x in [0, 1, 2]))

if callable(len):
    print(len('abc'))

print(isinstance(True, (bool, int)))

password = 'A1_2345'
only_alnum = all(c.isalnum() or c == '_' for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
allow_length = len(password) >= 6

print(all([only_alnum, has_upper, has_digit, allow_length]))

print(bytes([104, 101, 108, 108, 111]))
print(bytearray([104, 101, 108, 108, 111]))
