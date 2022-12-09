matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

newm=[]
# find the transpose of the matrix and print the result as shown in the example above
print("matrix:",matrix)

r=len(matrix)
c=len(matrix[0])

lismt=[]

for i in range(0,c):
        for j in range(0,r):
                lismt.append(matrix[j][i])

        newm.append(lismt)
        lismt=[]

print("transposed:",newm)
