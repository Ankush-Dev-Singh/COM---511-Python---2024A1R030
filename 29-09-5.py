# Reverse every kth row in a matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

# Input matrix
for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

k = int(input("Enter k: "))

# Reverse every kth row
for i in range(k - 1, rows, k):
    matrix[i].reverse()

# Display matrix
print("Matrix after reversing every kth row:")

for row in matrix:
    print(row)