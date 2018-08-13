# Assignment-3
'''
At this point, we have written code to generate a random hand and display that hand to the user.
We can also ask the user for a word (Python's input) and score the word (using your getWordScore).
However, at this point we have not written any code to verify that a word given by a
player obeys the rules of the game. A valid word is in the word list;
and it is composed entirely of letters from the current hand. Implement the is_validWord function.

Testing: Make sure the test_is_validWord tests pass. In addition, you will want to test your
implementation by calling it multiple times on the same hand - what should the correct behavior be?
Additionally, the empty string ('') is not a valid word - if you code this function correctly,
you shouldn't need an additional check for this condition.

Fill in the code for is_validWord in ps4a.py and be sure you've passed the appropriate
tests in test_ps4a.py before pasting your function definition here.
'''

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    var_c = 0
    var_l = len(word_list)

    if word in word_list:
        for i in hand:
            if i in word:
                var_c = var_c + 1
    print(var_c)
    if var_c == var_l:

        return True
    return False


def main():
    """main function"""
    word = input()
    var_n = int(input())
    adict = {}
    for i in range(var_n):
        data = input()
        var_l = data.split()
        adict[var_l[0]] = int(var_l[1])
    var_l2 = list(input().split())
    print(is_valid_word(word, adict, var_l2))



if __name__ == "__main__":
    main()
