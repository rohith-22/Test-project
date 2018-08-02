'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    string = input()
    length = len(string)
    count = 0
    i = 0
    while i <= length:
        if string[i:i + 3] == 'bob':
            count += 1
        i += 1
    print(count)
main()
