def  get_matrix(n, m, value):
    matrix = []
    for i in range(int(n)):
        matrix_s = []
        for j in range(int(m)):
            matrix_s.append(value)
        matrix.append(matrix_s)

    return matrix


result1 = get_matrix(2, 2, 10)
print(result1)
result2 = get_matrix(3, 2, 5)                     
print(result2)



