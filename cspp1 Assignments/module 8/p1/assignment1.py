"""# Exercise: Assignment-1
# Write a Python function, factorial(n),
that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number."""
def factorial(n_um):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_um == 0:
        return 1
    if n_um == 1:
        return 1
    return n_um * factorial(n_um - 1)
def main():
    """ main function """
    a_input = input()
    print(factorial(int(a_input)))
if __name__ == "__main__":
    main()
