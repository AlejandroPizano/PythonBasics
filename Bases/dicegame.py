import random
def rolldice():
    dice_total=random.randint(1,6)+random.randint(1,6)
    return dice_total
player1=input("Enter player 1 name: \n")
player2=input("Enter player 2 name: \n")
def main():
    roll= rolldice()
    roll2=rolldice()
    print(player1, "rolled", roll)
    print(player2, "rolled", roll2)
    if roll==roll2:
        print("TIE")
    elif roll>roll2:
        print(player1, "is the winner!!")
    else:
        print(player2," is the winner")

main()