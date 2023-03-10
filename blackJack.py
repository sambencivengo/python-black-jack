import random
import time

play_game = True
while play_game:

  player_In = True
  dealer_In = True
  def delay(amount=0.5):
    time.sleep(amount)


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
  def deal_card(hand, hit = False, dealer_hit = False):
    card = deck.pop(0) # the deck is shuffled so we can remove item at the top of the deck (index 0) and deal it into a hand
    hand.append(card)
    if hit:
      delay()
      print(f'\nYou have been dealt a {format_hands([card])}')
    if dealer_hit:
      delay()
      print(f'\nThe dealer has been dealt a card')

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
  def exposeDealerHand():
    delay()
    if player_In == False:
      return format_hands(dealer_hand)
    else:
      return format_hands([dealer_hand[0]])


  # GAME START
  deal_hands()

  def announce_start():
    print('Building deck of cards...')
    delay(amount=0.2)
    print('♥')
    delay(amount=0.2)
    print('♥', '♠')
    delay(amount=0.2)
    print('♥', '♠', '♦')
    delay(amount=0.2)
    print('♥', '♠', '♦', '♣')
    delay()

  announce_start()

  def format_hands(hand):
    res = []
    for card in hand:
      res.append(f"{card['val']} of {card['suit']}")
    return ', '.join(res)




  while player_In or dealer_In:
    if player_In:
      print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}')
    print(f'\nDealer reveals {exposeDealerHand()}\n')
    if player_In:
      standOrHit = input("1: Hit\n2: Stand\n")
    if standOrHit == '2':
      delay()
      player_In = False
    else:
      delay()
      print('\nYou have chosen to hit.')
      deal_card(player_hand, hit = True)
    if calculate_hand_value(player_hand) >= 21:
      break
    if not player_In:
      if calculate_hand_value(dealer_hand) > 17:
        dealer_In = False
      else: 
        deal_card(dealer_hand, dealer_hit=True)
      if calculate_hand_value(dealer_hand) >= 21:
        break  
    



  if calculate_hand_value(player_hand) == 21:
    print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('Blackjack! You win!')
  elif calculate_hand_value(dealer_hand) == 21:
    print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('Blackjack! Dealer wins.')
  elif calculate_hand_value(player_hand) > 21:
    print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('You bust! Dealer Wins.')
  elif calculate_hand_value(dealer_hand) > 21:
    print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('Dealer busts! You win!.')
  elif 21 - calculate_hand_value(dealer_hand) < 21 - calculate_hand_value(player_hand):
    print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('Dealer wins.')
  elif 21 - calculate_hand_value(dealer_hand) > 21 - calculate_hand_value(player_hand):
    print(f'\nYou have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('You win!.')
  else:
    print(f'You have {format_hands(player_hand)} for a total of {calculate_hand_value(player_hand)}.\n\nThe dealer has {format_hands(dealer_hand)} for a total of {calculate_hand_value(dealer_hand)}.')
    print('Game is a tie!')

  if play_game:
    play_again = input("\n\n1: Play Again?\n2: Quit\n")
  if play_again == '2':
    print('Thanks for playing!')
    play_game = False

