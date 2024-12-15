class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def join_game(self, game_name):
        print(f"Player {self.name} (age {self.age}) has joined the game: {game_name}!")

# Danh sách các trò chơi có sẵn
games = ["Chess", "Football", "Racing", "Puzzle"]

def get_input(prompt, input_type=str):
    """Hàm để lấy đầu vào từ người dùng với kiểm tra lỗi."""
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")

# Nhập thông tin người chơi
print("Welcome to the Game System!")
name = get_input("Enter your name: ", str)
age = get_input("Enter your age: ", int)

# Tạo một Player object
player = Player(name, age)

# Hiển thị danh sách trò chơi và chọn
print("\nAvailable games:")
for i, game in enumerate(games, start=1):
    print(f"{i}. {game}")

choice = get_input("Choose a game by entering the number (1-4): ", int)
if 1 <= choice <= len(games):
    selected_game = games[choice - 1]
    player.join_game(selected_game)
else:
    print("Invalid choice! Please restart and try again.")
