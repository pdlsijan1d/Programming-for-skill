def fibs(n):
    n = int(input("Enter no of terms you want:"))
    a = 0
    b = 1
    
    print(a, end=" ")
    print(b, end=" ")

    for i in range(0, n-2):
        c = a+b
        a=b
        b=c
        print(c, end=" ")

# Make sure there are absolutely NO spaces before this line!
fibs(5)


    