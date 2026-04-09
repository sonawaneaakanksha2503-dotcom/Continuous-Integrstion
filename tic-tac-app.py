import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables
current_player = "X"
board = [""] * 9

# Check winner
def check_winner():
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a,b,c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Button click
def on_click(i):
    global current_player
    
    if board[i] == "":
        board[i] = current_player
        buttons[i].config(text=current_player)
        
        winner = check_winner()
        
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                messagebox.showinfo("Game Over", f"{winner} Wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()