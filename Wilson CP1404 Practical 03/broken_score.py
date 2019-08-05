"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def get_score():
    score = float(input("Enter score: "))
    return score

def main():
    score = get_score()

    while score<0 or score>100:
        print("Invalid number")
        score = float(input("Enter score: "))

    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")

main()