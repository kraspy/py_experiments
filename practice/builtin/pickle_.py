import pickle

with open('file.pkl', 'wb') as f:
    pickle.dump({'a': 1}, f)
    pickle.dump({'b': 2}, f)
    pickle.dump({'c': 3}, f)


with open('file.pkl', 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
