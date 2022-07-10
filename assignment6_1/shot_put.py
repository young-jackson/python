def main():
    shots = input("Enter the lengths of the throws (m) separated by commas.\n").split(",")
    largest = 0
    if shots == [""]:
        print("No accepted results.")
    else:
        for shot in shots:
            if largest <= float(shot):
                largest = float(shot)
        print(f"The best result is {largest:0.2f} m.")


main()
