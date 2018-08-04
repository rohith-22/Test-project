'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    str_i = input()
    q = len(str_i)
    str_r = ""
    str_p = ""
    for k in range(q):
        print("1")
        if str_i[k] == '!':
            print(str_i[k])
            str_p = str_r + " "
        else:
        	print("2")
        	str_p = str_r + str_i[k]
        k += 1
    print(str_p)
if __name__ == "__main__":
    main()
