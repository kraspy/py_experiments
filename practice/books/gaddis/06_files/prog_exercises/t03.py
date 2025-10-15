import tempfile

_, fp = tempfile.mkstemp(text=True)

with open(fp, 'w') as f:
    f.writelines([s + '\n' for s in 'abcdef'])

with open(fp) as f:
    for i, line in enumerate(f, 1):
        print(f'{i}: {line}', end='')
