from typing import List 

class Card:
  def __init__(self, num, t):
    self.number: int = num
    self.t: str = t
  
  def __repr__(self):
    return f"{self.number} of {self.t}"

TYPES = ["clubs", "spades", "hearts", "diamond"]

def calc_score(cards: List[Card]) -> int:
  types = {
    "clubs": 0,
    "spades": 0,
    "hearts": 0,
    "diamond": 0
  }
  for card in cards:
    types[card.t] += 1

  score = 0
  for count in types.values():
    if count > 0:
      score += 2 ** count
  return score

# print(calc_score([Card(3, "hearts"), Card(4, "hearts"), Card(2, "spades")]))


def setup() -> set[Card]:
  deck: set[Card] = set()
  for t in TYPES:
    for n in range(1, 14):
      deck.add(Card(n, t))
  return deck

print(setup())