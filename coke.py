def main():
    amount = 0

    while amount < 50:
        print(f"Amount due: {50 - amount} cents")
        machine = int(input("Enter Coin in denominations of 25, 10, and 5 cents: "))
        if machine in (25, 10, 5):
            amount += machine
        else:
            print("Invalid coin. Please insert a coin denomination")
    print(f"Amount inserted: {amount} cents")


main()
