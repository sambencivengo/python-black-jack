import random


# values
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits= ['♥', '♠', '♦', '♣']

# empty deck
deck = []

def build_deck():
  for suit in suits:
    set_of_cards = []
    for card in card_values:
      card_props = {'val': card, 'suit': suit,}
      set_of_cards.append(card_props)
    deck.extend(set_of_cards)

build_deck()

# shuffle deck
random.shuffle(deck)

# empty player hands
# TODO: make quantity of players a variable
player_hand = []
dealer_hand = []

# deal cards
def deal_card(hand):
  card = deck.pop(0) # the deck is shuffled so we can remove item at the top of the deck (index 0) and deal it into a hand
  hand.append(card)

# automate the amount of times dealt with player counts
def deal_hands():
  deal_card(player_hand)
  deal_card(dealer_hand)
  deal_card(player_hand)
  deal_card(dealer_hand)

deal_hands()

# calculate hand value
def calculate_hand_value(hand):
  aces = []
  hand_value = 0
  for card in hand:
    if card['val'] == 'A':
      aces.append(card['val'])
    if type(card['val']) is int:
      hand_value += card['val']
    elif card['val'] in ['J', 'Q', 'K']:
      hand_value += 10
  for card in aces:
    if hand_value + 11 > 21:
      hand_value += 1
    else:
      hand_value += 11
  print({'value': hand_value, "hand": hand })

calculate_hand_value(player_hand)
calculate_hand_value(dealer_hand)

# show dealer hand


# determine winner


