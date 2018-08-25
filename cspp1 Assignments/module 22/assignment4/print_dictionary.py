'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    """ print"""
    sorted_list = sorted(dictionary)
    for each_element in sorted_list:
        print(each_element, "-", dictionary[each_element])

def main():
    """ input"""
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
