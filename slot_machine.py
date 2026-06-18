import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}




def deposit():
    while True:
        amount = input("Enter deposit amount: $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                return amount
            else:
                print("Deposit must be greater than 0.")
        else:
            print("Enter a valid number.")


def get_lines():
    while True:
        lines = input(f"Enter number of lines (1-{MAX_LINES}): ")

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Invalid number of lines.")
        else:
            print("Enter a valid number.")


def get_bet():
    while True:
        bet = input(f"Enter bet per line (${MIN_BET}-${MAX_BET}): ")

        if bet.isdigit():
            bet = int(bet)

            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f" ⚠️  bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Enter a valid number.")                                      




def get():
    new = []

    for i, count in symbol.items():
        for _ in range(count):
            new.append(i)

    columns = []

    for _ in range(COLS):
        column = []
        available = new[:]

        for _ in range(ROWS):
            value = random.choice(available)
            available.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):

    for row in range(ROWS):

        values = []

        for column in columns:
            values.append(column[row])

        print(" | ".join(values))



def winning(columns, lines, bet):

    total_win = 0

    for row in range(lines):

   
        if columns[0][row] == columns[1][row] == columns[2][row]:

            symbol = columns[0][row]

            win = symbol_value[symbol] * bet

            total_win += win

            print(f"Line {row + 1} won! (+${win})")

    return total_win


def play_again():
    while True:
        choice = input("\nPress Enter to spin again, or type 'q' to quit: ").strip().lower()

        if choice == "":
            return True
        elif choice == "q":
            return False
        else:
            print("Invalid input. Press Enter to continue or 'q' to quit.")


# ------------------ MAIN ------------------

def main():

    balance = deposit()

    while True:
        # Ask for number of lines each round
        lines = get_lines()

        while True:

            bet = get_bet()

            total_bet = bet * lines

            if total_bet > balance:
                print("Not enough balance.")
            else:
                break

        print("\nSpinning...\n")

        columns = get()

        print_slot_machine(columns)

        winnings = winning(columns, lines, bet)

        print(f"\nYou won: ${winnings}")

        balance = balance - total_bet + winnings

        print(f"Remaining Balance: ${balance}")

        if balance <= 0:
            print("\nYou're out of balance. Game over.")
            break

        if not play_again():
            print(f"\nThanks for playing! Final balance: ${balance}")
            break


main()