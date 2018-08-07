"""# Exercise: PowerRecr
# Write a Python function, var_recurPower(var_base, var_exp),
that takes in two numbers and returns the var_base^(var_exp) of given var_base and var_exp.
# This function takes in two numbers and returns one number.
"""
def var_recurpower(var_base, var_exp):
    '''
    var_base: int or float.
    var_exp: int >= 0
    returns: int or float, var_base^var_exp
    '''
    # Your code here
    if var_exp == 0:
        return 1
    return var_base * var_recurpower(var_base, (var_exp-1))
def main():
    ''' main function '''
    data = input()
    data = data.split()
    print(var_recurpower(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
