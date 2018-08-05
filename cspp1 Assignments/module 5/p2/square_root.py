# Write a python program to find the square root of the given number 
# using approximation method
def main():
    VAR_EPSILON = 0.01
    VAR_STEP = 0.1
    VAR_SQUARE = int(input())
    VAR_GUESS = 0.0
    while VAR_GUESS <= VAR_SQUARE:
        if abs(VAR_GUESS**2-VAR_SQUARE) < VAR_EPSILON:
            break
        else:
            VAR_GUESS += VAR_STEP
    print(str(VAR_GUESS))
if __name__== "__main__":
	main()