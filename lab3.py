# Nils Olsson, cssc0699
# Lab 3
#
# Data URL: https://www.kaggle.com/gagazet/path-of-exile-league-statistic
#
# Analysis objective:
# To plot the total number of characters in the SSF Harbinger HC ladder in the
# game Path of Exile per classes along with the number of those characters which
# are dead.
#
# A ladder is a ranking of player characters in a specific expansion of a game
# (in this case Path of Exile is the game and the ladder I'm interested in is
# SSF Harbinger HC).
#
# SSF stands for solo-self-found, which means these player characters can only
# interact with other players through chat, not within the game world itself. In
# a loot-based action RPG like Path of Exile this means that the player has
# access only to the items he finds and limited to playing by himself. Some
# players find this mode of play more fun than the standard, MMO-like, mode of
# play where players can form parties and trade items and currency. The
# immediate trade repercussion is that it may be much more difficult to build
# specialized characters; that is characters which rely on specific items.
#
# HC stands for hardcore. If a character in a hardcore ladder dies while
# playing, that character is lost for good (has one life).
#
# I wanted to see what classes were better favored for this style of play in
# this pass ladder in terms of total popularity but also in which classes died
# less-often.

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import copy

data = pd.read_csv('./poe_stats.csv')

ladder_query = 'SSF Harbinger HC'
ladder_data = data[data['ladder'] == ladder_query]
classes = data['class'].unique()
class_data = { c: ladder_data[ladder_data['class'] == c] for c in classes }

class_counts = np.array(list(len(class_data[c]) for c in classes))
class_dead_ratios = np.zeros(len(classes))
class_notdead_ratios = copy(class_dead_ratios)
for i, c in enumerate(classes):
    dead, notdead = class_data[c].dead.value_counts(True)
    class_dead_ratios[i] = dead
    class_notdead_ratios[i] = notdead

class_dead_counts = np.round(class_counts*class_dead_ratios)
class_notdead_counts = np.round(class_counts*class_notdead_ratios)

for i, c in enumerate(classes):
    count = class_counts[i]
    dead = class_dead_counts[i]
    notdead =class_notdead_counts[i]
    print(f'{c} Total:{count} Dead:{dead} Not dead:{notdead}')

ind = np.arange(len(classes))
p1 = plt.bar(ind, class_counts, label='Total')
p2 = plt.bar(ind, class_dead_counts, label='Count dead')

plt.title('''\
Number of dead versus not-dead characters per class
in Path of Exile SSF Harbinger HC ladder\
''')
plt.legend(loc='best')
plt.ylabel('Dead versus not dead')
plt.xticks(ind, classes, rotation='vertical')
plt.tight_layout()
plt.show()

