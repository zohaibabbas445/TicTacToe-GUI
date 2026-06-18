print("1. Script starting...")
import tkinter as tk
print("2. Tkinter imported...")
from tkinter import messagebox
print("3. Messagebox imported...")

class TicTacToe:
    def __init__(self, master):
        print("4. Initializing game class...")
        self.board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
        self.current_player = 'X'
        
        master.title("Tic Tac Toe - Python")
        master.geometry("400x450")
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    master, 
                    text=self.board[i][j], 
                    font=('Arial', 24), 
                    width=4, 
                    height=2,
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        self.turn_label = tk.Label(master, text=f"Player {self.current_player}'s turn", font=('Arial', 14))
        self.turn_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        reset_btn = tk.Button(master, text="New Game", font=('Arial', 12), command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3)
        print("5. GUI setup complete.")
    
    def on_click(self, row, col):
        if self.board[row][col] in ['X', 'O']:
            return
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player, state='disabled')
        
        if self.check_win():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins! 🎉")
            self.reset_game()
            return
        if self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw! 🤝")
            self.reset_game()
            return
        
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.turn_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_win(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2]:
                return True
            if b[0][i] == b[1][i] == b[2][i]:
                return True
        if b[0][0] == b[1][1] == b[2][2]:
            return True
        if b[0][2] == b[1][1] == b[2][0]:
            return True
        return False
    
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] not in ['X', 'O']:
                    return False
        return True
    
    def reset_game(self):
        self.board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
        self.current_player = 'X'
        self.turn_label.config(text=f"Player {self.current_player}'s turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.board[i][j], state='normal')

print("6. Class defined.")
if __name__ == "__main__":
    print("7. Running main...")
    root = tk.Tk()
    print("8. Window created.")
    game = TicTacToe(root)
    print("9. Game object created. Entering mainloop...")
    root.mainloop()
    print("10. Mainloop exited.")