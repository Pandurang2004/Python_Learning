print("\t\t\t Welcome to my Calculator!!!") 
#where \t is used in representing certain whitespace characters.

while True:
    print("1: Addition, 2: Subtraction, 3: Multiplication, 4: Division, 0: Exit")
    choice = input("Select the operation from above : ")
    if choice in ['1', '2', '3', '4', '0']:
       #if user enter 1'' i.e Addition
        if choice == '1':
            print("You are doing Addition !!")
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            try:
                a = float(a)
                b = float(b)
                print("Addition is:", a + b)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        
        #if user enter 2 i.e Subtraction
        elif choice == '2':
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            try:
                a = float(a)
                b = float(b)
                print("Subtraction is:", a - b)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        
        #if user enter the 3 i.e Multiflication
        elif choice == '3':
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            try:
                a = float(a)
                b = float(b)
                print("Multiplication is:", a * b)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        
        #if user enter 4 i.e Division
        elif choice == '4':
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            try:
                a = float(a)
                b = float(b)
                if b == 0:
                    #if the entered second number(divisor) is 0 then multiplication is not posible
                    print("Error! Cannot divide by zero.")
                else:
                    print("Division is:", a / b)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        
        elif choice == '0':
            print("\t Bye Bye \t See you \t again!!")
            break
    else:
        print("Invalid choice! Please select a valid option.")
