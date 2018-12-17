import pickle

with open('data_obj', 'rb') as fp:
    data = pickle.load(fp)

for line in data:
    print(line)
