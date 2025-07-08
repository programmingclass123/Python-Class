
guess = int(input("Guess the right number "))
secret_number = 8

while  guess != secret_number:
    print ("You have guessed wrong number. Please try again")
    guess = int(input("Guess the right number "))

print("you have guessed the right number")