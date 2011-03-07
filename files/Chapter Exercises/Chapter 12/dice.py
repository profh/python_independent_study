from random import randint

class Dice:

    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def values(self):
        return list(self.dice)

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randint(1,6)

    def rollAll(self):
        self.roll(range(5))

    def score(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif (not (3 in counts)) and (not (2 in counts)) \
             and (counts[1]==0 or counts[6] == 0):
            return "Straight", 20
        elif 3 in counts:
            return "Three of a Kind", 8
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0
        



