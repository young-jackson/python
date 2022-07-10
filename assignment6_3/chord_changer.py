
MAJOR_CHORDS = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def split_chord(chord):
    if chord[0:2] in MAJOR_CHORDS:
        return chord[0:2], chord[2:]
    elif chord[0] in MAJOR_CHORDS and chord[1] not in ["#", "b"]:
        return chord[0], chord[1:]
    else:
        return "", chord


def transpose(chord, semitones):
    trans_chord = split_chord(chord)
    if trans_chord[0] != "":
        base = MAJOR_CHORDS[(MAJOR_CHORDS.index(trans_chord[0]) + semitones) % 12]
        return base + trans_chord[1]
    else:
        return ""


def main():
    print("This program transposes your chords to a different key.\n"
          "Enter the chords of the song. Stop with an empty line.")
    chord_list = []
    latest_chord = input("Enter the first chord:\n")
    while latest_chord != "":
        if split_chord(latest_chord)[0] != "":
            chord_list.append(latest_chord)
        else:
            print("Unknown chord notation.")
        latest_chord = input("Enter the next chord:\n")

    upordown = input("Do you want to transpose up or down? (1 = up, 2 = down)\n")
    while upordown != "1" and upordown != "2":
        upordown = input("Choose one of the following: 1 = up, 2 = down\n")
    if upordown == "1":
        upordown = "up", 1
    else:
        upordown = "down", -1
    semitones = int(input(f"How many semitones do you want to transpose {upordown[0]}?\n")) * upordown[1]

    transposed_chords = []
    for chord in chord_list:
        transposed_chords.append(transpose(chord, semitones))
    print("Old chords -> New chords\n"
          "------------------------")
    for i in range(len(chord_list)):
        print(f"{chord_list[i]:11s}-> {transposed_chords[i]:10}")


main()


