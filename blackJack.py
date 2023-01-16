import random

player_In = True
dealer_In = True

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
  random.shuffle(deck)
  

build_deck()


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
  return(hand_value)


# show dealer hand, expose one card when second card is received. Once all players have chose to stand or bust, reveal hand
def exposeDealerHand(dealer_turn = False):
  if dealer_turn:
    return dealer_hand
  if len(dealer_hand) == 2:
    return dealer_hand[0]

# GAME START
deal_hands()


while player_In or dealer_In:
  print(f'Dealer reveals {exposeDealerHand()}')
  print(f'You have {player_hand} for a total of {calculate_hand_value(player_hand)}')
  if player_In:
    standOrHit = input("1: Stand\n2: Hit\n")
  if calculate_hand_value(dealer_hand) > 17:
    dealer_In = False
  else: deal_card(dealer_hand)
  if standOrHit == '1':
    playerIn = False
  else:
    deal_card(player_hand)
  if calculate_hand_value(player_hand) >= 21:
    break
  if calculate_hand_value(dealer_hand) >= 21:
    break

if calculate_hand_value(player_hand) == 21:
  print(f'\n You have {player_hand} for a total of {calculate_hand_value(player_hand)} and the dealer has {dealer_hand} for a total of {calculate_hand_value(dealer_hand)}.')
  print('Blackjack! You win!')
elif calculate_hand_value(dealer_hand) == 21:
  print(f'\n You have {player_hand} for a total of {calculate_hand_value(player_hand)} and the dealer has {dealer_hand} for a total of {calculate_hand_value(dealer_hand)}.')
  print('Blackjack! Dealer wins.')
elif calculate_hand_value(player_hand) > 21:
  print(f'\n You have {player_hand} for a total of {calculate_hand_value(player_hand)} and the dealer has {dealer_hand} for a total of {calculate_hand_value(dealer_hand)}.')
  print('You bust! Dealer Wins.')
elif calculate_hand_value(dealer_hand) > 21:
  print(f'\n You have {player_hand} for a total of {calculate_hand_value(player_hand)} and the dealer has {dealer_hand} for a total of {calculate_hand_value(dealer_hand)}.')
  print('Dealer busts! You win!.')
elif 21 - calculate_hand_value(dealer_hand) < 21 - calculate_hand_value(player_hand):
  print(f'\n You have {player_hand} for a total of {calculate_hand_value(player_hand)} and the dealer has {dealer_hand} for a total of {calculate_hand_value(dealer_hand)}.')
  print('Dealer wins.')
elif 21 - calculate_hand_value(dealer_hand) > 21 - calculate_hand_value(player_hand):
  print(f'\n You have {player_hand} for a total of {calculate_hand_value(player_hand)} and the dealer has {dealer_hand} for a total of {calculate_hand_value(dealer_hand)}.')
  print('You win!.')


