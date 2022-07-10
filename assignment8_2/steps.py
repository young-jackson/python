import datetime


def convert_text_to_date(date_as_text):
    """
    Parameter 'date_as_text' is a string that is given in following form:
    "DD.MM.YYYY", e.g. "15.5.2022"

    Function returns the date (datetime.date-object).
    """
    date_parts = date_as_text.split(".")
    day = int(date_parts[0])
    month = int(date_parts[1])
    year = int(date_parts[2])
    return datetime.date(year=year, month=month, day=day)


def print_file_contents(filename):
    """
    Prints the contents of the file 'filename'.
    """
    print()
    print("The contents of the file looks as follows:")
    print("-" * 100)
    file = open(filename, 'r')
    for line in file:
        print(line, end='')
    file.close()


def main():
    name_of_file = input("Enter the name of the file to be created for your step data:\n")
    file = open(name_of_file, "w")
    date = input("Enter the start date in format 'DD.MM.YYYY':\n")
    date_formatted = convert_text_to_date(date)

    total = 0
    span_days = 0
    print("Enter the number of steps (from walking/running) for each day. Stop with an empty line.")
    file.write("")
    steps = input(f"Enter the steps on {date_formatted}: ")
    while steps != "":
        total += int(steps)
        span_days += 1
        file.write(f"{date_formatted}: {steps}\n")
        date_formatted += datetime.timedelta(days=1)
        steps = input(f"Enter the steps on {date_formatted}: ")

    file.close()

    print("-" * 100)
    print(f"Step data saved successfully in the file '{name_of_file}'.")
    print(f"Saved the step data of {span_days} days.")
    if span_days != 0:
        print(f"Total number of steps from this period is {total} and daily average is {total / span_days:0.0f} steps.")

    print_file_contents(name_of_file)


main()
