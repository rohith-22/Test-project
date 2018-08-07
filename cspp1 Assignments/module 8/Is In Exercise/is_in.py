# Exercise: Is In
# Write a Python function, isIn(cha_r, g_str), that takes in two arguments a cha_racter and String and returns the isIn(cha_r, g_str) which retuns a boolean value.

# This function takes in two arguments cha_racter and String and returns one boolean value.

def isIn(cha_r, g_str):
    '''
    cha_r: a single cha_racter
    g_str: an alphabetized string
    
    returns: True if cha_r is in g_str; False otherwise
    '''
    a = None
    cha_r = cha_r.lower()
    s_str = g_str.lower()
    b_str = ''.join(sorted(s_str))
    if len(b_str) == 0:
        return "String length cannot be 0."
    elif len(b_str) == 1:
        if cha_r in b_str:
            return True
        return False
    else:
        a = int(len(b_str)/2)
        if cha_r == b_str[a]:
            return True
        else:
            if cha_r < b_str[a]:
                return isIn(cha_r,b_str[:a])
            return isIn(cha_r,b_str[a:])
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
if __name__== "__main__":
    main()
