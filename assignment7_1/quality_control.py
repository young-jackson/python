def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        product_file = open(filename,'r')
        count = [0, 0, 0]
        for line in product_file:
            line = line.rstrip()
            measure = float(line)
            if 4.52 <= measure <= 4.58:
                count[0] += 1
            elif 4.50 <= measure <= 4.60:
                count[1] += 1
            else:
                count[2] += 1
        product_file.close()

        print("File read successfully.")
        if count == 0:
            print("The file didn't contain any data.")
        else:
            print("The batch contained:")
            print(f"{count[0]} optimal ({count[0] / sum(count) * 100: 0.1f}%)")
            print(f"{count[1]} allowed ({count[1] / sum(count) * 100: 0.1f}%)")
            print(f"{count[2]} faulty ({count[2] / sum(count) * 100: 0.1f}%).")
            if count[2] / sum(count) <= 0.03:
                print("The batch passed the quality inspection.")
            else:
                print("The batch didn't pass the quality inspection.")

    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except ValueError:
        print("Incorrect number in the file '{:s}'. Program ends.".format(filename))


main()
