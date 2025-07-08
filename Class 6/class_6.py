a = int(input("Guess the right number: ")) 
secret_number = 9

while a != secret_number: 
    print("You have guessed the wrong number!")
    a = int(input("Guess the right number: "))

print("You have guessed the right number")
