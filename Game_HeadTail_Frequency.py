'''
GAME: HEAD TAIL FREQUENCY 
A coin is tossed 100 times.
Random value of Head or Tail can come.
Create the dictionary for the same and count
{'H':valueH,'T': valueT}
Count how many times heads and tails comes,
Plot frequency graph (histogram)


USE: random library: choice function
'''

import random as rd
import pandas as pd
import matplotlib.pyplot as plt

game = {'H':0,'T':0}
#game_list = []

for i in range(0,100):
	ch = rd.choice(['H','T'])
	if ch == 'H':
		game['H'] = game.get('H') + 1
	else:
		game['T'] = game.get('T') + 1
#	game_list.append(ch)

print 'Game Data: ', game
#print 'Game List: ', game_list

value = game.values()
keys = game.keys()
series = pd.Series(value,keys)
#series1 = pd.Series(game_list)

print '\n', series
#print '\n', series1


series.plot(kind = 'bar',color = 'green')
plt.show()

#plt.hist(series1)
#series1.plot(kind = 'hist',color = 'pink')

#plt.show()