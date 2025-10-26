class WTF: ...


print(hash(WTF()) == hash(WTF()))
print(id(WTF()) == id(WTF()))
