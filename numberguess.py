import random  

secret_number = random.randint(1, 100)

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 100.")

guess = None  
attempts = 0  

while guess != secret_number:
    guess = int(input("Take a guess: "))  
    attempts += 1  

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
