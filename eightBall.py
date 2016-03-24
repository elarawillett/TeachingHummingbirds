from random import randint

print("Please type a yes/no question and hit enter. ")

question = input()

randomNumber = randint(1,8)

if(randomNumber == 1):
        print("I wouldn't bet on it.")

elif(randomNumber == 2):
        print("Should you really ask that question?")

elif(randomNumber == 3):
        print("It is highly probable.")

elif(randomNumber == 4):
        print("Don't count on it.")

elif(randomNumber == 5):
        print("Ask again later.")

elif(randomNumber == 6):
        print("Never in a million years.")

elif(randomNumber == 7):
        print("Always.")

else:
        print("It could be.")
