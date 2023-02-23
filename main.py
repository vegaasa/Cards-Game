import random

suits = ("Diamonds","Clubs","Hearts","Spades")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {
    "Two":2,"Three":3,"Four":4,"Five":5,
    "Six":6,"Seven":7,"Eight":8,"Nine":9,
    "Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14
}

class Cards():
    "THIS CLASS IS FOR CARDS"

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f"Cards is {self.rank} {self.suit}"
    
class Deck():
    "THIS CLASS IS FOR CARDS IN PLAYER HANDS"
    def __init__(self):

        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                new_cards = Cards(suit,rank)
                self.all_cards.append(new_cards)

    def shuffle_cards(self):
        "THIS METHOD IS FOR SHUFFLE DECK"

        random.shuffle(self.all_cards)

    def deals_one(self):
        "THIS METHOD IS FOR DELETING ONE CARDS"

        return self.all_cards.pop()

class Player():
    "THIS CLASS IS FOR PLAYER(COMPUTER)"
    pass

