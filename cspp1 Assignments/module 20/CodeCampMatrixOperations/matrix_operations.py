"""matrices"""
def mult_matrix(m_1, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    row_m_1 = len(m_1)
    column_m_1 = len(m_1[0])
    row_m_2 = len(m_2)
    column_m_2 = len(m_2[0])
    product_of_matrices = []
    if column_m_1 == row_m_2:
        for i in range(row_m_1):
            product_row = []
            for j in range(column_m_2):
                sum_ = 0
                for l in range(row_m_2):
                    sum_ += int(m_1[i][l]) * int(m_2[l][j])
                product_row.append(sum_)
            product_of_matrices.append(product_row)
    else:
        print("Error: Matrix shapes invalid for mult")
        #print(product_of_matrices)
    return product_of_matrices
def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    row_m_1 = len(m_1)
    column_m_1 = len(m_1[0])
    row_m_2 = len(m_2)
    column_m_2 = len(m_2[0])
    sum_of_matrices = []
    if row_m_1 == row_m_2 and column_m_1 == column_m_2:
        for i in range(row_m_1):
            sum_rows = []
            for j in range(column_m_1):
                sum_rows.append(int(m_1[i][j]) + int(m_2[i][j]))
            sum_of_matrices.append(sum_rows)
        #print(sum_of_matrices)
    else:
        print("Error: Matrix shapes invalid for addition")

    return sum_of_matrices

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    #print('enter matrix')
    input_length = input()
    rows = int(input_length[0])
    columns = int(input_length[2])
    matrix_list = []
    i = 0
    while i < rows:
        input_row = input()
        new_list = input_row.split(" ")
        #print(new_list)
        if len(new_list) == columns:
            matrix_list.append(new_list)
        #print(matrix_list)
            i = i+1
        else:
            print('Error: Invalid input for the matrix')
            break
    return matrix_list

def main():
    """ main function """
    # read matrix 1
    matrix_1 = read_matrix()
    # read matrix 2
    matrix_2 = read_matrix()
    # add matrix 1 and matrix 2
    if matrix_1 == False or matrix_2 == False:
        return 'Error: Invalid input for the matrix'
    else:
        print(add_matrix(matrix_1, matrix_2))
    # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
