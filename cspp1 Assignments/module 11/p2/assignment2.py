"""#Exercise: Assignment-2
#Implement the update_hand function. Make sure this function has no side effects: i.e.,
it must not mutate the hand passed in. Before pasting your function definition here,
be sure you've passed the appropriate tests in test_ps4a.py.
"""
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    a_dict = {}
    for j in word:
        if j in hand:
            a_dict[j] = hand[j]-1
    return a_dict

def main():
    """main function"""
    var_n = input()
    adict = {}
    for i in range(int(var_n)):
        data = input()
        var_l = data.split()
        adict[var_l[0]] = int(var_l[1])
    data1 = input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
    main()
