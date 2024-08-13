# Print the all prime numbers between 1-100 . and give the addition of middle two prime numbers

L1=[]       #create empty list
for x in range(2,100):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=' ')
        L1.append(x) #adding each prime numbers in list L1
print()
length=len(L1) 
mid=length//2  #finding mid of list
print("Addition of middle two numbers :",L1[mid]+L1[mid-1])

