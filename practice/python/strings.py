for attr in str.__dict__:
    if not attr.startswith('_'):
        print(attr)

print(f'{1000.125:.>+#010,.2f}')
