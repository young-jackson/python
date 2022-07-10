def main():
    print("This is a vocabulary quiz.")
    file_name = input("Enter the name of the file used.\n")
    vocabulary = []
    try:
        file = open(file_name)
        for line in file:
            parts = line.rstrip().split(":")
            if len(parts) == 2 and "" not in parts:
                test_answer = parts[1].split("/")
                if "" not in test_answer:
                    vocabulary.append([parts[0], parts[1]])
                else:
                    print(f"ERROR in line:  {line}", end="")
            else:
                print(f"ERROR in line:  {line}", end="")
        print("Enter the following words in English:")

        remaining = list(range(len(vocabulary)))
        while len(remaining) != 0:
            for i in range(len(vocabulary)):
                if i in remaining:
                    word_tuple = vocabulary[i]
                    correct_words = word_tuple[1].split("/")

                    lower_correct_words = []
                    for word in correct_words:
                        lower_correct_words.append(word.lower())

                    answer = input(word_tuple[0] + "\n")
                    if answer.lower() in lower_correct_words:
                        print("Correct!")
                        remaining.remove(i)
                    else:
                        answer = input("Incorrect, try again!\n")
                        if answer.lower() in lower_correct_words:
                            print("That was correct.")
                        else:
                            print(f"Incorrect again, the correct answer is {correct_words[0]}")
            if len(remaining) != 0:
                print("Repeat the words which were incorrect:")
        print("Well done! The quiz terminates.")

    except OSError:
        print("ERROR in reading the file. The program terminates.")


main()
