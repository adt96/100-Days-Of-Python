"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
Hint
There are 365 days in a year, 52 weeks in a year and 12 months in a year.
Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_i=int(age)
year_diff=90-age_i
years_left=365*year_diff
weeks_left=52*year_diff
months_left=12*year_diff
print(f"You have {years_left} days, {weeks_left} weeks, and {months_left} months left.")

