def main():
    print("Enter 'VAR_H' to indicate the guess is too high.")
    print("Enter 'VAR_L' to indicate the guess is too low.")
    print("Enter 'VAR_C' to indicate I guessed correctly.")
    var_a = input("Enter a number between 0 and 100:")
    var_l = 0
    var_h = 100
    var_ans = (var_l + var_h)//2
    print(var_ans)
    var_a1 = input("Enter either of VAR_H,VAR_L,VAR_C:")
    while var_a1 != "var_c":
        if var_a1 == "var_l":
            var_l = var_ans
            var_ans = (var_l+var_h)//2
            print(var_ans)
            print("Is your secret number"+str(var_ans)+"?")
            print("If not Enter 'VAR_H' to indicate the guess is too high.")
            print("Enter 'VAR_L' to indicate the guess is too low.")
            print("Enter 'VAR_C' to indicate I guessed correctly.")
            var_a1 = input("Enter either of VAR_H,VAR_L,VAR_C:")
        else:
            var_h = var_ans
            var_ans = (var_l+var_h)//2
            print(var_ans)
            print("Is your secret number"+str(var_ans)+"?")
            print("If not Enter 'VAR_H' to indicate the guess is too high.")
            print("Enter 'VAR_L' to indicate the guess is too low.")
            print("Enter 'VAR_C' to indicate I guessed correctly.")
            var_a1 = input("Enter either of VAR_H,VAR_L,VAR_C:")
    print("Your guessed number is:", var_a)
main()