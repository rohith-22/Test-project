'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    s_dict = {}
    s_list = string.split(' ')
    for each_element in s_list:
        each_element = re.sub('[^a-zA-Z]',"",each_element)
        if each_element in s_dict:
            s_dict[each_element] += 1
        else:
            s_dict[each_element] = 1
    return s_dict
def main():
    input_n = int(input())
    string = ""
    for i in range(input_n):
        if string == '':
            string += input()
        else:
            string += ' ' + input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
