from typing import List 
from tkinter import * 

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

def setup() -> set[Card]:
  deck: set[Card] = set()
  for t in TYPES:
    for n in range(1, 14):
      deck.add(Card(n, t))
  return deck

print(setup())

window = Tk()
window.title("Google Project")
window.geometry('1200x400')
window.mainloop()
#window.tk.call('tk', 'scaling', 3.0)  - makes thesize of everything 3 times bigger

#x = Button(window, text="?????", command=func_name)  - creates a button
#x.grid(column=0, row=2) - place it in the window (learn how to)
#def func_name():
#  window.destroy() - for example
