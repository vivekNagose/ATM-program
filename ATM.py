print("Insert your Card")
CorrectPIN = int(1234)
i=1
while i<5:
    PIN=int(input("Enter your PIN - "))
    if PIN != CorrectPIN:
        print("Incorrect PIN, Try Again.")
        print("chances left - " + str(3-i))
        i+=1
        if i==4:
            print("Card blocked")
            break
    else:
        amount = input("Enter amount - ")
        print(amount)
