#Check the ATM pin is right or wrong . Give only 3 chances to enter pin to user. 

pin=7499
no_oftime=0
while no_oftime!=3:
    no_oftime=no_oftime+1
    p=int((input("Enter a pin:")))
    if p==pin:
        print("Transaction Successful!")
        print("THANK YOU!!!")
        break
    else:
        print("Invalid pin")
else:
    print("Card blocked")
        
    


