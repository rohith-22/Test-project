def var_payingdebtoffinayear(var_balance, var_annualinterestrate):
    """
    This function is using bi-section search
    """
    var_monthlyinterestrate = (var_annualinterestrate) / 12.0
    var_monthlypaymentlowerbound = var_balance / 12
    var_monthlypaymentupperbound = (var_balance * (1 + var_monthlyinterestrate)**12) / 12.0
    var_newbalance = var_balance
    var_epsilon = 0.0001
    var_guess = (var_monthlypaymentlowerbound + var_monthlypaymentupperbound)/2
    while True:
        var_month = 1
        while var_month <= 12:
            var_newbalance = var_newbalance - var_guess
            var_newbalance = var_newbalance + (var_monthlyinterestrate * var_newbalance)
            var_month += 1
        if var_newbalance > 0 and var_newbalance > var_epsilon:
            var_monthlypaymentlowerbound = var_guess
            var_newbalance = var_balance
        elif var_newbalance < 0 and var_newbalance < -var_epsilon:
            var_monthlypaymentupperbound = var_guess
            var_newbalance = var_balance
        else:
            return var_guess
        var_guess = (var_monthlypaymentlowerbound + var_monthlypaymentupperbound)/2
def main():
    """
    This function is to call the above
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(round(var_payingdebtoffinayear(data[0], data[1]), 2)))
if __name__ == "__main__":
    main()