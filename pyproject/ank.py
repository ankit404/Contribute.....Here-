import math
import random

print("let's start the number guessing game")

UL=int(input("Enter the upper limit: "))
LL=int(input("Enter the lower limit: "))

x=random.randint(LL,UL)

print("You have", round(math.log(UL-LL+1,2)),"no of chances")

count=0

while count< round(math.log(UL-LL+1,2)):
    count+=1

    guess=int(input("Enter your guessed number:"))

    if guess > x:
        print("Your guess is too high")
    elif guess < x:
        print("Your guess is too low")
    elif guess==x:
        print("Your guess is correct the number is", guess)
        break
if count>= round(math.log(UL-LL+1,2)):
    print("Your chances are over!\n the correct number is",x)



