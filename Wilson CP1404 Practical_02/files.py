"""The solutions for these programs are provided, to help you get going - or to confirm that your solution was valid.
Note: when you execute a Python program that contains a line like open('data.txt', 'w') the new file "data.txt" is created in the same folder as the Python file in your PyCharm project.

Create a new file called files.py and do all of the following in it:

Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

Create a text file called numbers.txt and save it in your prac_02 directory. Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write code that opens "numbers.txt", reads the numbers and adds them together then prints the result, which should be... 59.

Now write a fourth block of code that can print the total for a file containing any number of numbers."""

file_1=open("name.txt",mode="w")
name=str(input("Please input your name: "))
print(name, file=file_1)
file_1.close()

file_2=open("name.txt",mode="r")
print("Your name is ",file_2.read())
file_2.close()

file_3=open("numbers.txt", mode="r")
number1=int(file_3.readline())
number2=int(file_3.readline())
total=number1+number2
print(total)
file_3.close()

file_4=open("numbers2.txt", mode="r")
read=file_4.readline()
number_one,number_two,number_three,number_four=read.split()
result=int(number_one)+int(number_two)+int(number_three)+int(number_four)
print(result)

file_4.close()