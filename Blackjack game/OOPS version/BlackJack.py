import random

suits = ('Hearts', 'Club', 'Spade', 'Diamond')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank.capitalize()
        self.value = values[rank.capitalize()]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.deck.pop(0)
    
    def __str__(self):
        return f'New Deck created.'
    
class Player:

    def __init__(self, name, balance):
        self.name = name
        self.player_cards = []
        self.balance = balance

    def add_balance(self, amount):
        self.balance += amount

    def deduct(self, amount):
        self.balance -= amount

    def add_cards(self, game_cards):
        if type(self.player_cards) == type([]):
            self.player_cards.extend(game_cards)
        else:
            self.player_cards.append(game_cards)

    def __str__(self):
        return f"Hi! I'm {self.name}, I have {self.balance} worth of chips. Let's play BlackJack!"
        
    