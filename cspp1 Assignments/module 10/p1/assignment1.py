'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    var_a = list("abcdefghijklmnopqrstuvwxyz")
    var_b = sorted(letters_guessed)
    var_acopy = var_a[:]
    for i in var_acopy:
        if i in var_b:
            var_a.remove(i)
    return ''.join(var_a)
def main():
    '''
    Main function for the given program
    '''
    usr_inpt = input()
    usr_inpt = usr_inpt.split()
    data = []
    for var_char in usr_inpt:
        data.append(var_char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
    