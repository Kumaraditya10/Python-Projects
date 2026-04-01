import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner():
    global winner
    # All 8 possible winning combinations (rows, columns, diagonals)
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
        (0, 4, 8), (2, 4, 6)             # Diagonal
    ]
    
    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.destroy()

# Function to handle button clicks
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Function to switch between players X and O
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Main Window Setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Game Variables
current_player = "X"
winner = False

# Create 9 buttons using list comprehension
buttons = [tk.Button(root, text="", font=("normal", 20), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

# Arrange buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Label to show whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()