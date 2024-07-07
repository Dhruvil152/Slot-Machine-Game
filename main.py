import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def calculate_winnings(reels, lines, bet, values):
    total_winnings = 0
    winning_lines = []
    for line in range(lines):
        first_symbol = reels[0][line]
        for reel in reels:
            current_symbol = reel[line]
            if first_symbol != current_symbol:
                break
        else:
            total_winnings += values[first_symbol] * bet
            winning_lines.append(line + 1)

    return total_winnings, winning_lines

def generate_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    reels = []
    for _ in range(cols):
        reel = []
        available_symbols = all_symbols[:]
        for _ in range(rows):
            selected_symbol = random.choice(available_symbols)
            available_symbols.remove(selected_symbol)
            reel.append(selected_symbol)

        reels.append(reel)

    return reels

def display_slot_machine(reels):
    for row in range(len(reels[0])):
        for i, reel in enumerate(reels):
            if i != len(reels) - 1:
                print(reel[row], end=" | ")
            else:
                print(reel[row], end="")
        print()

def get_deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The deposit amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def select_number_of_lines():
    while True:
        lines = input(f"How many lines do you want to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a valid number.")

    return lines

def place_bet():
    while True:
        amount = input("Enter the bet amount for each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The bet amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount

def play_spin(balance):
    lines = select_number_of_lines()
    while True:
        bet = place_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. Your current balance is: ${balance}")
        else:
            break

    print(f"Betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    reels = generate_slot_machine_spin(ROWS, COLS, symbol_counts)
    display_slot_machine(reels)
    winnings, winning_lines = calculate_winnings(reels, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"Winning lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = get_deposit()
    while True:
        print(f"Current balance: ${balance}")
        choice = input("Press Enter to spin (or type 'q' to quitt): ")
        if choice == "q":
            break
        balance += play_spin(balance)

    print(f"You cashed out with ${balance}")

main()
