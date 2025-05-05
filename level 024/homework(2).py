
secret_number = 7
attempts = 3
while attempts > 0 :
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == secret_number:
        print ("You win")
        break
    else:
        attempts -= 1 
        if attempts > 0:
             print("Wrong number. Attempts left:", attempts) 
        else:
            print("You lose")