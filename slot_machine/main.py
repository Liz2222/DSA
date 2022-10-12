#constant value

MAX_LINES = 3



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


def get_number_of_lines():
    while True:
        linest= input("Enter number of lines you want to bet on(1-" + str(MAX_LINES) + "?")
        if amount.isdigit():
            amount= int(amount)
            if amount >0 :
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount


def main():

  balance = deposit()

main()