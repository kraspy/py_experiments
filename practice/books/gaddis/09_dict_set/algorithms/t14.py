import pickle

with open('mydata.dat', 'rb') as f:
    try:
        while True:
            print(pickle.load(f))
    except EOFError:
        pass
