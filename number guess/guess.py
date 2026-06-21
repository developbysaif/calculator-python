print("Welcome to the Number Guessing Game!")
secret = 10

num = int(input("take a guess:"))
for i in range(3):
    num = int(input("take a guess:"))   
    if num == secret:
        print("Good job! You guessed my number!")
        break
    num = int(input("take a guess:"))   
else:
    print("Sorry, the number I was thinking of was", secret)    

