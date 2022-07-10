def main():
    print("Enter the prices of items. Stop with a negative value.")
    i = 0
    s = 0
    expensive = 0
    affordable = 1000
    while i >= 0:
        s += i
        if i > expensive:
            expensive = i
        if 0 < i < affordable:
            affordable = i
        i = float(input())
    if s != 0:
        print(f"TAX: {s*14/114:.2f}")
        print(f"TOTAL: {s:.2f}\n")
        print(f"The most expensive item: {expensive:.2f}")
        print(f"The most affordable item: {affordable:.2f}")
    else:
        print("You did not enter any items.")


main()
