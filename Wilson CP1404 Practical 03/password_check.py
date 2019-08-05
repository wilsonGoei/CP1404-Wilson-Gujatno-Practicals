
def get_password():
    password = str(input("Please input your password: "))
    return password

def turn_asterisk(password):
    print("*"*len(password))

def main():
    password = get_password()
    asterisk = turn_asterisk(password)



main()