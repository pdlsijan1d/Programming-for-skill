def prime():
    n = int(input("Enter a number:"))
    count = 0
    
    for i in range(1, n+1):
        if(n % i == 0):
            count +=1

    if(count <= 1):
        print("It is neither prime nor composite.")
    elif(count == 2):
        print("Prime number.")
    else:
        print("Composite.")

prime()

        

