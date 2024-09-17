


def  get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_s = []
        for j in range(m):
            matrix_s.append(value)
        matrix.append(matrix_s)
    return matrix

n = int(input('Количество строк:'))
if n <= 0:
    while n <= 0:
        print ('количество строк не может быть отрицательным или равным нулю')
        n = int(input('Попробуйте еще раз:'))
m = int(input('Количество столбцов:'))
if m <= 0:
    while m <= 0:
        print ('количество столбцов не может быть отрицательным или равным нулю')
        m = int(input('Попробуйте еще раз'))
value = int(input('Значение элемента матрицы:'))
result1 = get_matrix(n, m, value)
print(result1)




