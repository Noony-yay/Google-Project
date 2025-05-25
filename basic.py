from typing import List, Set
from tkinter import * 
from random import sample

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

def setup() -> Set[Card]:
  deck: set[Card] = set()
  for t in TYPES:
    for n in range(1, 14):
      deck.add(Card(n, t))
  return deck

print(setup())

window = Tk()
window.title("Google Project - card game")
window.geometry('1200x400')

canvas = Canvas(window, width=1200, height=400, bg="green")
canvas.pack()

deck = list(setup())
user_cards = sample(deck, 5)
card_items = []
selected_cards = []

i = 0
for card in user_cards:
    x = 50 + i * 120
    y = 100
    rect = canvas.create_rectangle(x, y, x + 100, y + 150, fill="white", outline="black")
    label = canvas.create_text(x + 50, y + 75, text=str(card), font=("Arial", 10))
    card_items.append({"rect": rect, "text": label, "card": card})
    i += 1

def on_canvas_click(event):
    clicked = canvas.find_closest(event.x, event.y)[0]
    for item in card_items:
        if clicked == item["rect"] or clicked == item["text"]:
            if item["card"] in selected_cards:
                selected_cards.remove(item["card"])
                canvas.itemconfig(item["rect"], fill="white")
            else:
                selected_cards.append(item["card"])
                canvas.itemconfig(item["rect"], fill="lightblue")
canvas.bind("<Button-1>", on_canvas_click)

window.mainloop()
#window.tk.call('tk', 'scaling', 3.0)  - makes thesize of everything 3 times bigger

#x = Button(window, text="?????", command=func_name)  - creates a button
#x.grid(column=0, row=2) - place it in the window (learn how to)
#def func_name():
#  window.destroy() - for example
