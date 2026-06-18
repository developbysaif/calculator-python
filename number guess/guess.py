print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

secret = 10

num = int(input("take a guess:"))

if num == secret:
    print("Good job! You guessed my number!")

else:
    print("Sorry, the number I was thinking of was", secret)    

