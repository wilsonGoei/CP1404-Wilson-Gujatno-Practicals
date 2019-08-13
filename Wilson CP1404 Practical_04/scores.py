"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""

def scores_per_subject(score_values):
    subject_scores = []
    subject = len(score_values[0])
    for i in range(subject):
        scores_each_subject = []
        for scores in score_values:
            scores_each_subject.append(scores.pop(0))
        subject_scores.append(scores_each_subject)
    return subject_scores

def display_result(rearranged_by_subject,subjects):
    for j,scores_each_subject in enumerate(rearranged_by_subject):
        print(subjects[j],"Scores: ")
        for score in scores_each_subject:
            print("{:>2}".format(score))
        print("Max: {:3}".format(max(scores_each_subject)))
        print("Min: {:3}".format(min(scores_each_subject)))
        print("Average: {:6.2f}\n".format(sum(scores_each_subject)/len(scores_each_subject)))


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    rearranged_by_subject = scores_per_subject(score_values)
    display_result(rearranged_by_subject,subjects)


main()