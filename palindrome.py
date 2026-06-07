def pal():
    n = int(input("Enter a positive integer number:"))
    num = n
    rev = 0

    while(n!=0):
        digit = n % 10 
        rev = rev * 10 + digit
        n = n // 10

    if(rev) == num:
        print(f"{num} is palindrome.")
    else:
        print(f"{num} is not palindrome.")

pal()