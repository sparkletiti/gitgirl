#program that asks the user to enter his/her name and age and returns a message addressed to them that tells them the year they will turn 100 years old.

#name and age hold the user inputs.
name=input("Please enter your name:")
age= input ("Please enter your age: ")

#birth_year holds the year he/she was born and year_of_100 is the year he/she will turn 100 years.
birth_year = 2019 - int(age)
year_of_100 = birth_year +100

print ("Hi " + name + ", you will turn 100 years old in " + str(year_of_100))

#A programme to determine whether the number input by the user is an odd or even number
A_number = input ("Enter a number:")

if int(A_number)%2 ==1:
	print (A_number + " is an odd number")
else:
	print (A_number + " is an even number")