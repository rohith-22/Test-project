# Write a python program to find the square root of the given number
# using approximation method
def main():
    var_epsilon = 0.01
    var_step = 0.1
    var_square = int(input())
    var_guess = 0.0
    while var_guess <= var_square:
        if abs(var_guess**2-var_square) < var_epsilon:
            break
        else:
            var_guess += var_step
    print(str(var_guess))
if __name__ == "__main__":
    main()
