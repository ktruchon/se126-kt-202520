class Card:
  def __init__(cardFace, face, suit):
    cardFace.face = face
    cardFace.suit = suit


deck = []

import csv 

with open("text_files\cards.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:

        deck.append(Card(rec[1], rec[0]))

for i in range(0, len(deck)):
  print(f"{deck[i].face}{deck[i].suit}")



