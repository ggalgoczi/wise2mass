#!/usr/bin/env python
import numpy as npy
from numpy import *
import math
import scipy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from pylab import figure, show


Cut=-1.7
GxFilename = 'DataGx'
StarFilename = 'DataStars'
ColumnOfWise1_Gx = 7
ColumnOf2MASS_Gx = 4
ColumnOfWise1_Star = 7
ColumnOf2MASS_Star = 4
GalaxiesIdentifiedCorrectly, GalaxiesIdentifiedIncorrectly, StarsIdentifiedInCorrectly, StarsIdentifiedCorrectly = 0,0,0,0


def graph(x1todo, y1todo, x2todo, y2todo):  
	plt.xlabel('W1-J')
	plt.ylabel('W1') 
	
	
#	line1 = matplotlib.lines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="red")
#	plt.legend((line1),('Thing 1'),numpoints=1, loc=1)

#	plt.legend(["ro","bo"], ["Galaxies", "Stars"])
	x1 = npy.array(x1todo)  
	x2 = npy.array(x2todo)  
	y1 = npy.array(y1todo)  
	y2 = npy.array(y2todo)
	
#	line_up, = plt.plot(x1,y1, label='Line 2')
#	line_down, = plt.plot(x2,y2, label='Line 1')
#	plt.legend([line_up, line_down], ['Line Up', 'Line Down'])

	plt.plot(x1, y1, 'ro', x2, y2, 'bo')  
	plt.show()

#Open data of galaxies
DataGalaxies = genfromtxt(GxFilename)
N = len(DataGalaxies)
W1 = []
J = []

for i in range(N):
	W1.append(DataGalaxies[i][ColumnOfWise1_Gx])
	J.append(DataGalaxies[i][ColumnOf2MASS_Gx])

#Open data of NOT galaxies
DataStar = genfromtxt(StarFilename)
N2 = len(DataStar)
W1_Star = []
J_Star = []

for j in range(N2):
	W1_Star.append(DataStar[j][ColumnOfWise1_Star])
	J_Star.append(DataStar[j][ColumnOf2MASS_Star])

##### Calculate effectivity
W1_num = [float(x) for x in W1]
J_num = [float(x) for x in J]
W1_Star_num = [float(x) for x in W1_Star]
J_Star_num = [float(x) for x in J_Star]

DifferenceGx = [x - y for x, y in zip(W1_num, J_num)]
DifferenceStars = [x - y for x, y in zip(W1_Star_num, J_Star_num)]

for i in range(N):
	if DifferenceGx[i] <= Cut:
		GalaxiesIdentifiedCorrectly += 1
	else:
		GalaxiesIdentifiedIncorrectly += 1

for i in range(N2):
	if DifferenceStars[i] <= Cut:
		StarsIdentifiedInCorrectly += 1
	else:
		StarsIdentifiedCorrectly += 1

print 'The % of galaxies identified correctly',100*GalaxiesIdentifiedCorrectly/(GalaxiesIdentifiedCorrectly+GalaxiesIdentifiedIncorrectly),'%'
print 'Star contamination:',100*StarsIdentifiedInCorrectly/(StarsIdentifiedInCorrectly+GalaxiesIdentifiedCorrectly),'%'

### PLOT
#Gx = mpatches.Patch(color='red', label='The red data')
#plt.legend([red_dot]handles=[Gx])
#	plt.plot(W1-J, W1, 'ro', markersize = 2, W1_Star-J_Star, W1_Star, 'bo', markersize = 2)


graph(DifferenceGx, W1_num, DifferenceStars, W1_Star_num)

