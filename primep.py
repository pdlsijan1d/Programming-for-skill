n = int(input("Print prime numbers up to: "))

# Loop through every number from 1 to n
for i in range(1, n + 1):
    count = 0  # Reset count for EVERY new number 'i'
    
    # Check how many numbers divide 'i' perfectly
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            
    # If it has exactly 2 factors (1 and itself), it's prime
    if count == 2:
        print(i, end=" ")