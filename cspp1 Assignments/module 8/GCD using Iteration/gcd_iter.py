"""# Exercise: GCDIter
# Write a Python function, gcdIter(a, b),
that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number."""
def var_gcditer(var_a, var_b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    var_r = 1
    while var_r != 0:
        var_r = var_a % var_b
        var_a = var_b
        var_b = var_r
    return var_a
def main():
    """ mvar_ain function"""
    data = input()
    data = data.split(' ')
    print(var_gcditer(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
