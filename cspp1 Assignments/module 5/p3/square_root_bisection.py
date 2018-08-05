# Write a python program to find the square root of the given number
# using Bi-section method
def main():
    num_a = int(input())
    var_epsilon = 0.01
    var_low = 0.0
    var_high = num_a
    bi_val = (var_high + var_low)/2.0
    while abs(bi_val**2 - num_a) > var_epsilon:
        if bi_val**2 < num_a:
            var_low = bi_val
        else:
            var_high = bi_val
        bi_val = (var_high + var_low)/2.0
    print(bi_val)
if __name__ == "__main__":
    main()
