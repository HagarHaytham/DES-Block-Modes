import des_modes
from common import getBlockMode,desKey
import time
import matplotlib.pyplot as plt
import numpy as np


one_block = 'abcdefgh'
Nblocks = [1,2,4,8,16,24,32,64,128,256,512,1024]
modes = [2,3]
data = [[] for i in range(2)]
    
for mode in modes:
    ModeOfOperation = getBlockMode(mode)
    for block in Nblocks:
        msg = block * one_block
        start_time= time.time() #start timer
        cipherText=ModeOfOperation.encrypt(desKey,msg)
        end_time= time.time() #end timer
        taken_time= end_time - start_time
        data[mode-2].append(taken_time)
color_list = ['b', 'c']
labels = ['CBC','CFB']
gap = .8 / len(data)
for i, row in enumerate(data):
  X = np.arange(len(row))
  plt.bar(X + i * gap, row,
    width = gap,
    color = color_list[i % len(color_list)],
    label = labels[i])

plt.xticks([r + gap for r in range(len(Nblocks))], Nblocks)
plt.ylabel('Time Taken For Encryption')
plt.xlabel('No. of blocks')

plt.legend()
plt.show()
