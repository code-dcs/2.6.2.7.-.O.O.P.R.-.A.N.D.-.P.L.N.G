def numberInputs(printOut, choice_type):
    while True:
        try:
            return choice_type(input(printOut))
        except ValueError:
            print(
                "\n\n\n\n\n[ Invalid input! Please enter a valid choice number. ]\n")


while True:
    JavaScore = numberInputs("Input:\nJava Score: ", int)
    CScore = numberInputs("Input:\nC Score: ", int)
    DBScore = numberInputs("Input:\nDatabase Handling Score: ", int)

    score = (JavaScore + CScore + DBScore) / 3
    gradeLetter = ""
    gradeMin, gradeMax = 0, 0

    if score >= 90:
        gradeLetter = "A"
        gradeMin, gradeMax = 90, 100
    elif score >= 80:
        gradeLetter = "B"
        gradeMin, gradeMax = 80, 89
    elif score >= 75:
        gradeLetter = "C"
        gradeMin, gradeMax = 75, 79
    elif score >= 0:
        gradeLetter = "F"
        gradeMin, gradeMax = 0, 75
    else:
        gradeLetter = "Out of range"

    if 0 <= score <= 100:
        print(f"\nAverage: {score:.2f}")
        if 75 < gradeMax <= 100:
            print("Grade: " + gradeLetter + " because the average is between " +
                  str(gradeMin) + " and " + str(gradeMax))
        else:
            print("Grade: " + gradeLetter + " because the average 75 and below")
    else:
        print("Grade invalid")

    print("\nDo you want to continue: (YES / NO)")
    exitChoice = input()
    if exitChoice.strip().lower() == "no":
        print("Program terminated.\nThank you!")
        break

    print("\n")
