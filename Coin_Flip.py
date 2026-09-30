import random

print("================================")
print("       COIN FLIP GAME")
print("================================")

heads = 0
tails = 0
playing = 1

print("Welcome to the Coin Flip Game!")
print("You can flip the coin as many times as you want.")
print("Press Enter to flip the coin.")
print("Type q to stop the game.")

while playing == 1:

    answer = input("\nPress Enter to flip or type q to quit: ")

    if answer == "q":
        playing = 0
    else:
        coin = random.randint(1, 2)

        if coin == 1:
            print("The coin landed on HEADS!")
            heads = heads + 1
        else:
            print("The coin landed on TAILS!")
            tails = tails + 1

        total = heads + tails

        print("Total flips:", total)
        print("Heads:", heads)
        print("Tails:", tails)

print("\n================================")
print("          FINAL RESULT")
print("================================")

print("Total flips:", heads + tails)
print("Total Heads:", heads)
print("Total Tails:", tails)

if heads > tails:
    print("Heads appeared more times.")
elif tails > heads:
    print("Tails appeared more times.")
else:
    print("Heads and Tails appeared equally.")

print("Thank you for playing!")
print("================================")
