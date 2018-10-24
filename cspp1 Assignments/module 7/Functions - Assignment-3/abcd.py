def payingdebt_offin_a_year(balance, annual_interest_rate):
    '''input 320000 0.2
    output: 29157.09'''
    previous_balance = balance
    monthly_interest_rate = annual_interest_rate/12
    monthly_payment_lowerbound = previous_balance/12
    monthly_payment_upperbound = (previous_balance*(1+monthly_interest_rate)**12)/12.0
    epsilon = 0.03
    while abs(balance) > epsilon:
        monthly_payment = (monthly_payment_lowerbound+monthly_payment_upperbound)/2
        balance = previous_balance
        for _ in range(12):
            monthly_unpaid_balance = (balance) - (monthly_payment)
            balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
        if balance > epsilon:
            monthly_payment_lowerbound = monthly_payment
        elif balance < -epsilon:
            monthly_payment_upperbound = monthly_payment
    return str(round(monthly_payment, 2))

def main():
    ''' this functon is used to print the lowest payment value'''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingdebt_offin_a_year(data[0], data[1]))

if __name__ == "__main__":