# Exercise: Assignment-2
# Write a Python function, sumofdigits,
#that takes in one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.
def sumof_digits(var_p):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    while var_p >= 0:
        if var_p == 0:
            return 0
        return (var_p % 10) + sumof_digits(var_p // 10)
def main():
    """
    This function is to call the sumofdigits function
    """
    var_q = input()
    print(sumof_digits(int(var_q)))
if __name__ == "__main__":
    main()
