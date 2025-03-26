import random
from class_card import Card, suits,ranks,values

class Deck:

    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        try:
            return self.all_cards.pop()
        except IndexError:
            print('All cards are dealt.')
    
    def __str__(self):
        return 'New Card deck created.'

if __name__ == '__main__':

    new_deck = Deck()

    print(new_deck)

    new_deck.shuffle()
    for card_object in new_deck.all_cards:
        pass #print(card_object)

    print(len(new_deck.all_cards))
    mycard = new_deck.deal_one()
    print(mycard)
    print(len(new_deck.all_cards))

    for i in range(0,len(new_deck.all_cards)+1):
        #print(new_deck.all_cards[i])
        new_deck.deal_one()
