def main():
    numberofchildren = int(input("How many heights will be entered?\n"))
    while numberofchildren <= 0:
        print("Enter a positive value!")
        numberofchildren = int(input("How many heights will be entered?\n"))
    p = 0
    print("Enter the heights of the children on separate lines.")
    for i in range(numberofchildren):
        child = int(input())
        if child >= 140:
            p += 1
    print(f"There are {numberofchildren} children.")
    print(f"{p} of the children are allowed and {numberofchildren - p} are not allowed on the roller coaster.")


main()
