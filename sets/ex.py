# A 2 3 4 5 6 7 8 9 10 J Q K
# spades hearts diamonds clubs

class Card:
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rankList[self.rank] + " of " + self.suitList[self.suit])

threeOfClubs = Card(1, 11)

print(threeOfClubs)

threeOfClubs.suitList[1] = "ass"
print(threeOfClubs)


