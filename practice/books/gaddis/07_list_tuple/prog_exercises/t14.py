import matplotlib.pyplot as plt

with open('expenses.txt') as f:
    expenses = dict(line.strip().split(':') for line in f.readlines())

plt.pie(list(expenses.values()), labels=list(expenses.keys()))

plt.show()
