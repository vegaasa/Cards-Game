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
    def __init__(self,name):
        self.name = name
        self.all_cards = list()

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):

        if type(new_cards) == type([]):
            #If new cards is multiple cards
            self.all_cards.extend(new_cards)
        else:
            #if new cards is single cards
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."



# INTIATE PLAYER
player_one = Player("Player One")
player_two = Player("Player Two")

new_deck = Deck()
new_deck.shuffle_cards()

### Give Each Player Cards
for x in range(26):
    player_one.add_cards(new_deck.deals_one())
    player_two.add_cards(new_deck.deals_one())

#SET UP GAME
game_on = True
counter = 0

while game_on:
    counter += 1
    print(f"This is Round {counter}")

    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Player Two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Player One wins!")
        game_on = False
        break

    ## Add Cards to table
    player_one_cards = [] 
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        ### Check Player 1
        print(f"THIS WAR IS PLAYER ONE CARDS : {player_one_cards[-1].value} vs PLAYER TWO CARDS : {player_two_cards[-1].value}")
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print("THIS ROUND IS WON BY PLAYER ONE ")
            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print("THIS ROUND IS WON BY PLAYER TWO ")
            at_war = False

        else:
            print("WAR")
            if len(player_one.all_cards) < 5:
                print("Player One unable to follow the war")
                print("PLAYER TWO WINS")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to follow the war")
                print("PLAYER ONE WINS")
                game_on = False
                break
            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
