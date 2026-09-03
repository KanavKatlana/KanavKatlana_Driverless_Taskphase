def multiply_matrices():
    print("Matrix A ")
    rows_A = int(input("Enter number of rows for Matrix A: "))
    cols_A = int(input("Enter number of columns for Matrix A: "))
    
    matrix_A = []
    print("Enter the elements row by row:")
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            val = int(input(f"Element [{i}][{j}]: "))
            row.append(val)
        matrix_A.append(row)


    print("Matrix B ")
    rows_B = int(input("Enter number of rows for Matrix B: "))
    cols_B = int(input("Enter number of columns for Matrix B: "))
    
    matrix_B = []
    print("Enter the elements row by row:")
    for i in range(rows_B):
        row = []
        for j in range(cols_B):
            val = int(input(f"Element [{i}][{j}]: "))
            row.append(val)
        matrix_B.append(row)

    
    if cols_A != rows_B:
        print("\nError: Matrix multiplication is impossible!")
        print(f"Columns of Matrix A ({cols_A}) must equal Rows of Matrix B ({rows_B}).")
        return

    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            row.append(0)
        result.append(row)

    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A): 
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    
    print("\nResultant Matrix:")
    for row in result:
        print(row)


multiply_matrices()
