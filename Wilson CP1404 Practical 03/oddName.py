"""Wilson Goei Gujatno"""


def get_name():
    global name
    name = str(input("Please input your name: "))
    return name

def main():
    name = get_name()
    while name == "":
        print("Input cannot be blank")
        name = str(input("Please input your name: "))

    print(name[0::2])
    print(name[0::1])
    print(name[0::3])

main()
