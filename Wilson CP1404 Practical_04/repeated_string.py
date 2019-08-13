
strings = []


def repeating_string():
    strings_size = len(strings)
    same = []
    for i in range(0,strings_size):
        for j in range (i+1,strings_size):
            if strings[i] == strings [j]:
                same.append(strings[i])

    return same



def main():
    while True:
        string = str(input("Please input a string:\n>>>"))
        if string == "":
            break
        else:
            strings.append(string)
    result = 0
    result = sum([1 for x in strings if x == x]) >= 2
    if result == 1:
        repeat_strings = repeating_string()
        print("Strings repeated: ")
        for i in repeat_strings:
            print(i, end=" ")
    else:
        print("No repeated strings entered")




main()