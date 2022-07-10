import random

SPADE = "\u2660"
HEART = "\u2661"
DIAMOND = "\u2662"
CLUB = "\u2663"

SUITS = [SPADE,HEART,DIAMOND,CLUB]
FACES = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
FACES_AS_VALUES = {"2":2, "3":3, "4":4,"5":5,"6":6,"7":7,"8":8,\
                   "9":9,"10":10,"J":10,"Q":10,"K":10,"A":[11,1]}


def initialize_random():
    seed = int(input("Give seed for random generator:\n"))
    random.seed(seed)


def initialize_deck():
    deck = []
    for face in FACES:
        for suit in SUITS:
            card = [face,suit]
            deck.append(card)
    return deck


def shuffle_and_deal(deck):
    random.shuffle(deck)
    dealer = []
    player = []
    for i in range(2):
        player.append(deck.pop())
        dealer.append(deck.pop())
    return deck, player, dealer

# Implement the missing functions here


def hand_value(hand):
    total = 0
    aces = 0
    for n in hand:
        if n[0] != "A":
            total += FACES_AS_VALUES[n[0]]
        else:
            aces += 1
            total += 1
    while aces > 0 and total <= 11:
        total += 10
        aces -= 1
    return total


def print_hand_and_value(text, hand):
    print(f"--------------\n{text} hand:")
    printline = ""
    for n in hand:
        printline += n[0] + n[1] + " "
    print(printline)
    print(f"Value: {hand_value(hand)}")
    print("--------------")


def print_dealer_start_hand(hand):
    print(f"--------------\nDealer hand:")
    printline = "XX "
    for n in hand[1:]:
        printline += n[0] + n[1] + " "
    print(printline)
    print("--------------")


def main():
    print("Welcome to play the Twenty-One card Game!")
    print("Try to get closer to 21 than the dealer without going over 21.")
    initialize_random()
    deck = initialize_deck()
    deck, player_hand, dealer_hand = shuffle_and_deal(deck)
    bust = False
    print_dealer_start_hand(dealer_hand)
    print_hand_and_value("Your", player_hand)
    print("Let's continue onto draws.")

    if hand_value(player_hand) == 21:
        input("You have a natural 21. Press enter to continue onto dealer draws.\n")
    else:
        prompt = input("Do you want to draw another card? (y/n)\n")
        while prompt == "y":
            print("You draw another card.")
            player_hand.append(deck.pop())
            print_hand_and_value("Your", player_hand)
            if hand_value(player_hand) < 21:
                prompt = input("Do you want to draw another card? (y/n)\n")
            elif hand_value(player_hand) == 21:
                print("You reached 21! Can't draw anymore now.")
                input("Press enter to continue.\n")
                prompt = "n"
            else:
                print("You went bust. Dealer won.")
                bust = True
                prompt = "n"

    if not bust:
        print("Dealer opens their hand.")
        print_hand_and_value("Dealer", dealer_hand)
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            input("The dealer draws another card. Press enter to continue.\n")
            print_hand_and_value("Dealer", dealer_hand)

        if hand_value(dealer_hand) > 21:
            print("Dealer went bust. You won.")
        else:
            input("Press enter to see final hands.\n")
            print("Final hands:")
            print_hand_and_value("Dealer", dealer_hand)
            print_hand_and_value("Your", player_hand)
            if hand_value(player_hand) < hand_value(dealer_hand) <= 21:
                print("Dealer won")
            elif hand_value(dealer_hand) == hand_value(player_hand):
                print("It's a tie.")
            else:
                print("You won")


main()
