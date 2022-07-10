def main():
    meeting_year = int(input("What year did you meet?\n"))
    current_year = int(input("What is the current year?\n"))
    while current_year < meeting_year:
        print("The current year must be greater than or equal to the year you met.")
        meeting_year = int(input("What year did you meet?\n"))
        current_year = int(input("What is the current year?\n"))
    print("All your years together:")

    for i in range(1, current_year - meeting_year + 2):
        if i % 15 == 0:
            print("epic year")
        elif i % 5 == 0:
            print("big year")
        elif i % 3 == 0:
            print("happy year")
        else:
            print(i + meeting_year - 1)


main()

