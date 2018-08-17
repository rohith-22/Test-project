'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
filename ="/Users/rohithkumar/Desktop/git/cspp1/Test-project/cspp1 Assignments/module 16/CodeCampDocumentDistance/stopwords.txt"
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(input):
    stop_words = load_stopwords(filename)
    lower_case = input.lower()
    # clean_up = re.sub("[^a-z]", "",lower_case)
    #strip_input = clean_up.strip()
    list_words = lower_case.split(' ')
    list_copy = list_words.copy()
    for each_word in list_words:
        list_words[each_word] = re.sub("[^a-z]", "",each_word)

    list_copy = list_words.copy()
    for each_word in list_copy:
        if each_word in stop_words:
            list_words.remove(each_word)
    return list_words
# input1 = input()
# print(word_list(input1))

def word_dict(input):
    a_dict ={}
    input_word_list = word_list(input)
    for each_word in input_word_list:
        if each_word in a_dict:
            a_dict[each_word] +=1
        else:
            a_dict[each_word] = 1
    return a_dict
# input1 = input()
# print(word_dict(input1))
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary_1 = word_dict(dict1)
    #print(dictionary_1)
    dictionary_2 = word_dict(dict2)
    dict_3 = {}
    numerator = 0
    sum_1 = 0
    sum_2 = 0
    for each_word in dictionary_1:
        if each_word not in dict_3:
            dictionary_2[each_word] = 0
        if each_word not in dict_3:
            dict_3[each_word] = [dictionary_1[each_word], dictionary_2[each_word]]
    for each_word in dictionary_2:
        if each_word not in dict_3:
            dictionary_1[each_word] = 0
        if each_word not in dict_3:
            dict_3[each_word] = [dictionary_1[each_word], dictionary_2[each_word]]
    print(dict_3)
    for each_word in dict_3:
        numerator += dict_3[each_word][0] * dict_3[each_word][1]

        sum_1 += (dict_3[each_word][0]) ** 2
        sum_2 += (dict_3[each_word][1]) ** 2

    denominator = (math.sqrt(sum_1)) * (math.sqrt(sum_2))

    return (numerator/denominator)

# input1 = input()
# print(similarity(input1))

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
