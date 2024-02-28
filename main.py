import random

#Global, constant
MAX_LINES = 3   
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":4,
    "B":6,
    "C":8,
    "D":10
}
symbol_value = {
    "A":8,
    "B":6,
    "C":4,
    "D":2
}

#Generate items to slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):   #pick random value for each row in column
        column = []
        current_symbols = all_symbols[:] #copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns): #transpose matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:  # making sure "|" is not at the last column
                print(column[row], end=" | ") #End allows to print in the same row
            else:
                print(column[row], end="")
        print()

#Slot machine math
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]  #check if the symbol at each row is the same as the 1st one
            if symbol != symbol_to_check:
                break
        else:                               #Checking for each row, then go to winnings or return 0
            winnings+= values[symbol]*bet
            winnings_lines.append(line+1)

    return winnings, winnings_lines

    

#User input
def deposit():
    while True:
        amount = input("What would You like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("You must enter a number")       
    return amount

def get_numbers_of_lines():
    while True:
        lines = input("Enter the numbers of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid number")
        else:
            print("You must enter a number")       
    return lines

def get_bet():
    while True:
        bet = input("What would You like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("You must enter a number")       
    return bet

def spin(balance):
    lines = get_numbers_of_lines()

    while True:  #Checking balance
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else:
            break
 
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print (f"You won $",winnings)
    print (f"You won on lines:", *winning_lines)

    return winnings - total_bet

#Main loop
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play.(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()
