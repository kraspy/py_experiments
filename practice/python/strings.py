for attr in str.__dict__:
    if not attr.startswith('_'):
        print(attr)

print(f'{1000.125:.>+#010,.2f}')


print(
    ord('A'),
    chr(65),
    'A'.encode(encoding='utf-8'),
    b'\x41'.decode(encoding='utf-8'),
    sep='\n',
)
