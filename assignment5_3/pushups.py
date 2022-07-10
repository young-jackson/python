def main():
    print("This program analyzes your daily pushup history. Enter a negative amount when finished.")
    days = [int(input("How many push-ups did you do the first day?\n"))]

    no_days = False
    if days[0] < 0:
        print("You did not enter any data.")
        no_days = True

    while days[len(days) - 1] >= 0:
        latest = int(input("How many push-ups did you do the next day?\n"))
        days.append(latest)

    days.pop(len(days) - 1)

    if not no_days:
        print("Bar graph:")
        for i in range(len(days)):
            print(f"Day {i + 1:3d}:", "#" * days[i])
        print(f"\nIn total, you performed {sum(days)} pushups, which is roughly {sum(days) / len(days):.1f} per day.")
        print(f"The highest daily number of pushups was {max(days)} on day {days.index(max(days)) + 1}.")


main()
