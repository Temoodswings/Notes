import numpy
from matplotlib import pyplot as plt
x = [0.06,
0.12,
0.18,
0.24,
0.3,
0.36,
0.42]
y = [1.35,
5.8,
13.65,
24.75,
39.15,
57.05,
78.25]
plt.title("S-t Graph")
plt.xlabel("TIME(s)")
plt.ylabel("DISPLACEMENT(cm)")
plt.errorbar(x, y, yerr=0.05)
plt.show