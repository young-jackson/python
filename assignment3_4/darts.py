def main():
    print("Welcome to the darts calculator! I will keep track of your game of darts.")
    maximum = int(input("What is the start score of the game?\n"))
    rounds = 1
    currentpoints = maximum

    while rounds <= 11:
        roundpoints = currentpoints
        print(f"\nEnter the results of your throws for round {rounds}:")

        for i in range(1, 4):
            p = int(input(f"Throw {i}: "))
            currentpoints -= p

        if currentpoints < 0 or currentpoints == 1:
            print(f"You have reduced your score to {currentpoints}. Score resetting to the initial score of the round.")
            currentpoints = roundpoints
            print(f"You have {currentpoints} points remaining.")
        else:
            print(f"You have {currentpoints} points remaining.")
            if currentpoints == 0:
                print(f"You have won the game after {rounds} rounds. Congratulations!")
                rounds = 100
        
        rounds += 1


main()
