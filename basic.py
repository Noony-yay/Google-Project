class Card:
  def __init__(self, num, t):
    self.number: int = num
    self.t: str = t

def calc_score(cards: list[Card]) -> int:
  types = {
    "clubs": 0,
    "spades": 0,
    "hearts": 0,
    "diamond": 0
  }
  for card in cards:
    types[card.t] += 1
   
  return types
  
print(calc_score([Card(3, "hearts"), Card(4, "hearts"), Card(2, "spades")]))
