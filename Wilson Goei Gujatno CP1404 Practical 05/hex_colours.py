HEX_COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc", "BLACK": "#000000",
               "BROWN": "#a52a2a", "CORAL": "#ff7f50", "CYAN1": "#00ffff", "DARKGREEN": "#006400",
               "FIREBRICK": "#b22222", "GHOSTWHITE": "#f8f8ff", "GRAY": "#bebebe"}

colour = str(input("Enter colour name: ")).upper().replace(" ", "")

while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name")
    colour = str(input("Enter colour name: ")).upper().replace(" ", "")
