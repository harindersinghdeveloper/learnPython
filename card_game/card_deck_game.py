import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        #self.cards = [Card(suit, rank) for rank in ranks for suit in suits]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

new_deck = Deck()
new_deck.shuffle()
my_card = new_deck.deal()
print(my_card)
print(len(new_deck.cards))

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_one(self):
        return self.cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)


    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards'

player_one = Player('Harry')
player_two = Player('Anuj')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal())
    player_two.add_cards(new_deck.deal())

print(player_one)
print(player_two)

game_on = True
round_count = 0
cards_on_the_floor = []
while game_on:
    round_count += 1
    print(f'Round {round_count}')
    if len(player_one.cards) == 0:
        print(f'Game Over, {player_two.name} has won the game !!')
        game_on = False
        break
    if len(player_two.cards) == 0:
        print(f'Game Over, {player_one.name} has won the game !!')
        game_on = False
        break

    player_one_on_hand_card = player_one.remove_one()
    player_two_on_hand_card = player_two.remove_one()

    if player_one_on_hand_card.value > player_two_on_hand_card.value:
        if cards_on_the_floor:
            player_one.add_cards(cards_on_the_floor)
            cards_on_the_floor = []
        player_one.add_cards(player_one_on_hand_card)
        player_one.add_cards(player_two_on_hand_card)

    elif player_one_on_hand_card.value < player_two_on_hand_card.value:
        if cards_on_the_floor:
            player_two.add_cards(cards_on_the_floor)
            cards_on_the_floor = []
        player_two.add_cards(player_one_on_hand_card)
        player_two.add_cards(player_two_on_hand_card)

    else:
        print('At War!!')
        cards_on_the_floor.append(player_one_on_hand_card)
        cards_on_the_floor.append(player_two_on_hand_card)

print(player_one)
print(player_two)





