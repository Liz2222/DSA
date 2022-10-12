#constant value

MAX_LINES = 3
MAX_BET=10
MIN_BET=1


#input test code

def deposit():
    while True:
        amount= input("what would you like to deposit? $")
        if amount.isdigit():
            amount= int(amount)
            if amount >0 :
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_bet():
    while True:
        amount= input("what would you like to bet? $")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <=MAX_BET :
                break
            else:
                print(f"Amount must be between ${MAX_BET} - ${MIN_BET} .")
        else:
            print("Please enter a number")

    return amount



def get_number_of_lines():
    while True:
        lines= input("Enter number of lines you want to bet on(1-" + str(MAX_LINES) + "? ")
        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines


def main():

  balance = deposit()
  lines= get_number_of_lines()
  bet=get_bet()

  print(balance,lines,bet)

main()