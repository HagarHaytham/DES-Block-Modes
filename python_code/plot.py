import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

blocks = [1,2,3,4,5,6]
ECB = [12,13,14,14,15,6]
CBC = [1,21,13,41,22,5]
CFB = [14,11,6,7,12,5]
CTR = [2,4,6,8,8,7]

data = [ECB,CBC,CFB,CTR]

color_list = ['b', 'g', 'r','c']
labels = ['ECB', 'CBC','CFB','CTR']
gap = .8 / len(data)
for i, row in enumerate(data):
  X = np.arange(len(row))
  plt.bar(X + i * gap, row,
    width = gap,
    color = color_list[i % len(color_list)],
    label = labels[i])

plt.xticks([r + 0.25 for r in range(len(blocks))], blocks)
plt.ylabel('Time Taken For Encryption')
plt.xlabel('No. of blocks')

plt.legend()
plt.show()