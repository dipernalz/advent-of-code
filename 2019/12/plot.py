import matplotlib.pyplot as plt

x, y = [], []
with open('data.txt', 'r') as f:
    for l in f:
        s = l.split()
        x.append(s[0])
        y.append(s[1])

plt.plot(x, y)
plt.show()
