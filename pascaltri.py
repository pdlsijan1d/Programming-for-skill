def pascaltri():
    n = int(input("Enter the no of rows you want:"))
    triangle = []

    for i in range(0, n+1):
        row = []
        for j in range(0, i+1):
            if( j == 0 or j == i):
                row.append(1)
            else:
                left_above  = triangle[i-1][j-1]
                right_above = triangle[i-1][j]
                row.append(left_above + right_above)
        triangle.append(row)

    for row in triangle:
        for number in row:
            print(number, end=" ")
        print()

pascaltri()       
    






    