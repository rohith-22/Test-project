'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    """ frequency"""
    sorted_list = sorted(dictionary)
    for each_element in sorted_list:
        #dictionary[each_element] = ''
        for i in range(dictionary[each_element]):
            if '#' not in str(dictionary[each_element]):
                dictionary[each_element] = '#'
            else:
                dictionary[each_element] += "#"
        print(each_element, "-", dictionary[each_element])

def main():
    """ input """
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
