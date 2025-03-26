suits = ('Hearts', 'Club', 'Spade', 'Diamond')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
        'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        
        return f"{self.rank} of {self.suit}"
    
if __name__ == '__main__':

    #Create 2 cards

    two_of_hearts = Card('Hearts','Two')
    three_of_clubs = Card('Clubs','Three')
    
    print(two_of_hearts)
    print(three_of_clubs)

    print(two_of_hearts.value > three_of_clubs.value)
    #import random
    #Creating a dictionary of dynamically named variables as dict keys & 'Card' type as dict values
    
    cards = {}
    for suit in suits:
        for rank in ranks:
            card_name = f"{rank}_of_{suit}"
            cards[card_name] = Card(suit,rank)
    
    #taking key names indivudually and printing out the '__str__' for the card class for each key.
    for card_var_name in cards.keys():
        print(cards[card_var_name])