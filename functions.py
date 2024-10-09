def StandardDeck():
  """
  Initializes a standard 52 card deck and returns a list of tuples. Each tuple is a card
  """
  card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
  d = [(card, category) for category in card_categories for card in cards_list]
  return d


def card_value(card):
  """
  Returns the given card value

  Parameters: (card,description)
    A tuple which contains the card value and suit

  Returns: int
    Returns the card value as an integar
  """
  if card[0] in ['Jack', 'Queen', 'King']:
    return 10
  elif card[0] == 'Ace':
    return 11
  else:
    return int(card[0])


def prob(pS,deck):
  """
  Determines if the player should hit or stand based on the expected value if staying less than or equal to 21.

  Parameters: tuple, deck
      The players cards and the deck of remaining cards

  Returns: boolean
      Returns True for either hit or stand
  """
  h = False
  s = False
  r = 21 - pS
  count = 0

  for i in range (0,len(deck)):
    if card_value((deck[i])) <= r:
      count = count + 1

  chances = count/len(deck)
  #print(count)
  #print(len(deck))
  #print(chances)

  ###> Expected Value of hitting
  p1 = chances
  p2 = 1-chances
  w1 = 2
  w2 = -1
  E = p1*w1 + p2*w2

  #print(E)
  if E>0:
    #print("Hit")
    h = True
    s = False
  else:
    #print("Stand")
    s = True
    h = False
  return h,s


def prob_d(pS,deck):
  """
  Detmerines if the player should hit, stand, or double. The hit or stand is based on the probability as stated in 'def prob'. 
  The double is based on the expected value being greater than 1, meaning that the return would be more profitable.

  Parameters: tuple, deck
      The players cards and the deck of remaining cards

  Returns: boolean
      Returns True for either hit, stand, or double
  """
  h = False
  s = False
  d = False
  r = 21 - pS
  count = 0

  for i in range (0,len(deck)):
    if card_value((deck[i])) <= r:
      count = count + 1

  chances = count/len(deck)
  #print(count)
  #print(len(deck))
  #print(chances)

  ###> Expected Value of hitting
  p1 = chances
  p2 = 1-chances
  w1 = 2
  w2 = -1
  E = p1*w1 + p2*w2

  #print(E)
  if E>0:
    if (E>1) and (E<2):
      #print("Double")
      h = False
      s = False
      d = True
    else:
      #print("Hit")
      h = True
      s = False
      d = False
  else:
    #print("Stand")
    s = True
    h = False
    d = False
  return h,s,d

###> Hit, Stand, Double
def prob2(pS,deck,dS):
  count = 0
  count1 = 0
  h = False
  s = False
  d = False
  r = 21 - pS
  r1 = 21-dS

  for i in range (0,len(deck)):
    if card_value((deck[i])) <= r:
      count = count + 1
    if card_value((deck[i])) <=r1:
      count1 = count1 + 1

  chances = count/len(deck)
  chances1 = count1/len(deck)
  #print(count)
  #print(len(deck))
  #print(chances)

  ###> Expected Value of hitting
  p1 = chances
  p2 = 1-chances
  w1 = 2
  w2 = -1
  E = p1*w1 + p2*w2

  p3 = chances1
  p4 = 1-chances1
  w3 = 2
  w4 = -1
  E1 = p3*w3 + p4*w4
  #print(E)
  #print(E1)

  if (pS>11) & (E > 0) & (E1 > 0) & (E1>E):
    #print("Stand")
    h = False
    s = True
    d = False
  elif E>0:
    if (E>1) and (E<2):
      #print("Double")
      h = False
      s = False
      d = True
    else:
      #print("Hit")
      h = True
      s = False
      d = False
  else:
    #print("Stand")
    s = True
    h = False
    d = False
  return h,s,d