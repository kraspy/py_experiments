import pickle

dct = {'a': 1, 'b': 2}

with open('mydata.dat', 'ab') as f:
    pickle.dump(dct, f)
    print('pickled done!')
