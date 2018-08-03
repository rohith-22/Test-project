"""# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube"""
def main():
    var_s = int(input("number ="))
    var_i = 0
    while var_i ** 3 < var_s:
        var_i += 1
    if var_i ** 3 == var_s:
        print(str(var_s) + " " +"is a perfect cube")
    else:
        print(str(var_s) + " " + "is not a perfect cube")
main()
