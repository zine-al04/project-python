import os

# ================== UTILS ==================
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ================== MENU ==================
class Menu:

    def display_menu(self):
        print("Welcome to my X-O game!")
        menu_text = """
1. Start Game
2. Quit Game
Enter your choice (1 or 2): 
"""
        choice = input(menu_text)
        clear_screen()
        return choice

    def display_end_menu(self):
        menu_text = """
1. Restart Game
2. Quit Game
Enter your choice (1 or 2): 
"""
        choice = input(menu_text)
        clear_screen()
        return choice


# ================== PLAYER ==================
class Player:
    def __init__(self, symbol):
        self.name = ""
        self.symbol = symbol

    def choose_name(self):
        while True:
            name = input("Enter player name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")


# ================== BOARD ==================
class Board:

    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def restart_board(self):
        self.board = [str(i) for i in range(1, 10)]

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()


# ================== GAME ==================
class Game:

    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.menu = Menu()
        self.current_player = 0

    def start_game(self):
        choice = self.menu.display_menu()
        if choice == "1":
            self.setup_game()
            self.play_game()
        else:
            self.quit_game()

    def setup_game(self):
        for i, player in enumerate(self.players, start=1):
            print(f"Player {i} ({player.symbol})")
            player.choose_name()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()

            if self.check_win() or self.check_draw():
                choice = self.menu.display_end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            else:
                self.switch_player()

    def play_turn(self):
        player = self.players[self.current_player]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")

        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number.")

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_win(self):
        b = self.board.board
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_combinations:
            if b[combo[0]] == b[combo[1]] == b[combo[2]]:
                self.board.display_board()
                winner = self.players[self.current_player]
                print(f"🎉 Congratulations {winner.name}! You win!")
                return True
        return False

    def check_draw(self):
        if all(not cell.isdigit() for cell in self.board.board):
            self.board.display_board()
            print("🤝 It's a draw!")
            return True
        return False

    def restart_game(self):
        self.board.restart_board()
        self.current_player = 0

    def quit_game(self):
        print("Thank you for playing! 👋")


# ================== RUN ==================
game = Game()
game.start_game()
