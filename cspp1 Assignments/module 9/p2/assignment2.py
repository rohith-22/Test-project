'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
'''
def get_guessed_word(s_ecret_word, letters_guessed):
    '''
    s_ecret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in s_ecret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for i in s_ecret_word:
        if i not in letters_guessed:
            s_ecret_word = s_ecret_word.replace(i, "_")
    return s_ecret_word

def main():
    '''
    Main function for current assignment
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
    print(get_guessed_word(s_ecret_word, list1))

if __name__ == "__main__":
    main()
