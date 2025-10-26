print((a := 1, 2))
print(a)

# Фильтрация с извлечением
if (b := len('123')) == 5:
    ...
print(b)

# Считывание строк из файла по одной
with open(path := __file__) as f:
    while line := f.readline():
        ...

print(path)

# В аргументах функции
len(a := (lambda: 'abc')())

print(a)
