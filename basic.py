from typing import List # I only understood that the problem was that the phyton here isn't in the newest version so we needed to import "List"

class Card:
  def __init__(self, num, t):
    self.number: int = num
    self.t: str = t

def calc_score(cards: List[Card]) -> int: # here is the only change
  types = {
    "clubs": 0,
    "spades": 0,
    "hearts": 0,
    "diamond": 0
  }
  for card in cards:
    types[card.t] += 1

  #I also added the calculation of the score :-)
  score = 0
  for count in types.values():
    if count > 0:
      score += 2 ** count
  return score

print(calc_score([Card(3, "hearts"), Card(4, "hearts"), Card(2, "spades")]))
