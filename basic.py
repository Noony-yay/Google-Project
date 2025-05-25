window = Tk()
window.title("Card Game")
window.geometry("1200x500")

canvas = Canvas(window, width=1200, height=400, bg="green")
canvas.pack()


card_items = []  
selected_cards = []


deck = list(setup())
user_cards = sample(deck, 5)

for i, card in enumerate(user_cards):
    x = 50 + i * 150
    y = 100
    rect = canvas.create_rectangle(x, y, x + 100, y + 150, fill="white", outline="black")
    text = canvas.create_text(x + 50, y + 75, text=str(card), font=("Arial", 10))
    card_items.append({"rect": rect, "text": text, "card": card})

def on_canvas_click(event):
    clicked = canvas.find_closest(event.x, event.y)[0]
    for item in card_items:
        if clicked in [item["rect"], item["text"]]:
            card = item["card"]
            if card in selected_cards:
                selected_cards.remove(card)
                canvas.itemconfig(item["rect"], fill="white")
            elif len(selected_cards) < 5:
                selected_cards.append(card)
                canvas.itemconfig(item["rect"], fill="lightblue")
            break
    update_button_state()

canvas.bind("<Button-1>", on_canvas_click)

def send_cards():
    print("You sent:")
    for c in selected_cards:
        print(c)
    window.destroy()

def update_button_state():
    if len(selected_cards) == 5:
        send_btn.config(state="normal")
    else:
        send_btn.config(state="disabled")

send_btn = Button(window, text="Send Cards", command=send_cards, state="disabled")
send_btn.pack(pady=10)

window.mainloop()
