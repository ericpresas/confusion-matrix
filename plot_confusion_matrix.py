#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
from pylab import *

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
labels = ['a', 'b', 'c']

proportions = [1. * row / sum(row) for row in matrix]

figure()
# Keep major ticks labeless
xticks(range(len(labels)), [])
yticks(range(len(labels)), [])
# Place labels on minor ticks
gca().set_xticks([x + 0.5 for x in range(len(labels))], minor=True)
gca().set_xticklabels(labels, rotation='90', fontsize=10, minor=True)
gca().set_yticks([y + 0.5 for y in range(len(labels))], minor=True)
gca().set_yticklabels(labels[::-1], fontsize=10, minor=True)
# Finally, hide minor tick marks...
gca().tick_params('both', width=0, which='minor')
# Plot heat map
pcolor(array(proportions[::-1]), cmap=cm.Blues)
# Plot counts as text
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[::-1][y][x] != 0:
            text(x + 0.5, y + 0.5, matrix[::-1][y][x],
                 fontsize=9,
                 horizontalalignment='center',
                 verticalalignment='center')

grid(True)
title('Confusion matrix')
tight_layout()
show()
