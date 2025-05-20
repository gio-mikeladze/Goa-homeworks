num=int(input("Enter a number: "))
for i in range(2, (num)):
    if num==1:
        print("num is not prime")
    elif num %i==0:
        print("num is not prime")
    else:
        print("num is prime")