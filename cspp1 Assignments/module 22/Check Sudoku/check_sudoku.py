'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
# def check_r_c(sub_sudoku):
#     for each in sub_sudoku:
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # sudoku_a = []
    for each in sudoku:
        for each_element in each:
            if int(each_element) > 9:
                return False
    for each in sudoku:
        if each.count(each_element) > 1:
            return False
    for i in range(9):
        sudoku_column = []
        for j in range(9):
            sudoku_column.append(sudoku[i][j])
            for each in sudoku_column:
                if each.count(each_element) > 1:
                    return False
    sub_sudoku_1 = []
    sub_sudoku_2 = []
    sub_sudoku_3 = []
    sub_sudoku_4 = []
    sub_sudoku_5 = []
    sub_sudoku_6 = []
    sub_sudoku_7 = []
    sub_sudoku_8 = []
    sub_sudoku_9 = []
    for i in range(3):
        for j in range(3):
            sub_sudoku_1.append(sudoku[i][j])
        for each in sub_sudoku_1:
            if sub_sudoku_1.count(each) > 1:
                return False
        for j in range(3 ,6):
            sub_sudoku_2.append(sudoku[i][j])
        for each in sub_sudoku_2:
            if sub_sudoku_2.count(each) > 1:
                return False
        for j in range(6, 9):
            sub_sudoku_3.append(sudoku[i][j])
        for each in sub_sudoku_3:
            if sub_sudoku_3.count(each) > 1:
                return False
    for i in range(3,6):
        for j in range(3):
            sub_sudoku_4.append(sudoku[i][j])
        for each in sub_sudoku_4:
            if sub_sudoku_4.count(each) > 1:
                return False
        for j in range(3 ,6):
            sub_sudoku_5.append(sudoku[i][j])
        for each in sub_sudoku_5:
            if sub_sudoku_5.count(each) > 1:
                return False
        for j in range(6, 9):
            sub_sudoku_6.append(sudoku[i][j])
        for each in sub_sudoku_6:
            if sub_sudoku_6.count(each) > 1:
                return False
    for i in range(6,9):
        for j in range(3):
            sub_sudoku_7.append(sudoku[i][j])
        for each in sub_sudoku_7:
            if sub_sudoku_1.count(each) > 1:
                return False
        for j in range(3 ,6):
            sub_sudoku_8.append(sudoku[i][j])
        for each in sub_sudoku_8:
            if sub_sudoku_8.count(each) > 1:
                return False
        for j in range(6, 9):
            sub_sudoku_9.append(sudoku[i][j])
        for each in sub_sudoku_9:
            if sub_sudoku_9.count(each) > 1:
                return False

    # print(sub_sudoku_9)
    return True
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()