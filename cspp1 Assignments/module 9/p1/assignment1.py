'''
Exercise: Assignment-1
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''


def is_word_guessed(s_ecret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    c_oun_t = 0
    for i in s_ecret_word:
        if i in letters_guessed:
            var_a = s_ecret_word.replace(i, "#")
            s_ecret_word = var_a
            c_oun_t += 1
    if c_oun_t == len(s_ecret_word):
        return True
    return False
def main():
    '''
    Main function for the program
    '''
    usr_inpt = input()
    if usr_inpt:
        data = usr_inpt.split()
        s_ecret_word = data[0]
    else:
        data = []
        s_ecret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(s_ecret_word, list1))
if __name__ == "__main__":
    main()
    