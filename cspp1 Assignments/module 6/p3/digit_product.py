'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    int_input = int(input())
    int_input_a = int_input
    if int_input < 0:
        int_input_a = -int_input
    str_i = str(int_input_a)
    product = 1
    for i in str_i:
        product = product * int(i)
    if int_input < 0:
        print(-product)
    else:
        print(product)
if __name__ == "__main__":
    main()
