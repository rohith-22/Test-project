'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    input_n = int(input())
    list_a = []
    for each_input in range(input_n):
    	list_a.append(input())
    for each_element in range(len(list_a)):
    	print(list_a[each_element])

if __name__ == '__main__':
    main()
