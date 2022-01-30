# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
word1=['t','r','u','e']
word2=['l','o','v','e']

"""
loop through word1
get count of each variable 
add it to sum
"""

def word_count(word):
    sum=0
    word1=word
    for i in word1:
        sum += name1.count(i)
    for i in word1:
        sum += name2.count(i)
    return sum

main_sum1=str(word_count(word1))
main_sum2=str(word_count(word2))
total=int(main_sum1+main_sum2)

if(total<10 or total>90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif(total>40 and total<50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")



