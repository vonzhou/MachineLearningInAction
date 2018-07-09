# -*- coding: UTF-8 -*-

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import kNN

fig = plt.figure()
ax = fig.add_subplot(111)

datingDatMat, datingClassLabels = kNN.file2matrix('datingTestSet2.txt')

# ax.scatter(datingDatMat[:, 1], datingDatMat[:, 2])
ax.scatter(datingDatMat[:, 1], datingDatMat[:, 2], 15.0 * array(datingClassLabels), 15.0 * array(datingClassLabels))
plt.show()
