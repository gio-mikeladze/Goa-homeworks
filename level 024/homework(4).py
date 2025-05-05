hidden_number=5
atempts=3
while atempts>0:
    number_guessed=int(input("Enter a number:"))
    if hidden_number == number_guessed:
        print("you win")
    else:
        atempts=atempts-1
    if hidden_number!=number_guessed:
        print("wrong guess atempts left:",(atempts))
        if atempts==0:
            print("you lose")