from class_deck import Deck

class Player():

    def __init__(self, name):
         self.all_cards = []
         self.name = name

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
         
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
    
if __name__ == '__main__':

    new_player = Player('Avinash')

    print(type(new_player))
    print(new_player)

    new_deck = Deck()
    new_deck.shuffle()

    mycard = new_deck.deal_one()

    new_player.add_cards(mycard)

    print(new_player)
    print(new_player.all_cards[0])

    new_cards = []
    for i in range(0,4):
        new_cards.append(new_deck.deal_one())

    new_player.add_cards(new_cards)

    print(new_player)
    for cards in new_player.all_cards:
        print(cards)

    print(len(new_deck.all_cards))