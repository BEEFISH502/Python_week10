##3. Write a program that calculates a users Utility bill
'''
Math:
Cost  = kwh * rate
Subtotal = Cost + flat service fee

inputs will be:
1. total kwh used
2. rate per kwh
3. flat service fee

output:
-total bill amount

functions:
1. calculate_cost(kwh + rate)
2. subtotal(rate + flat fee)

'''
#this calculates the cost price of our total usage
def calc_cost(kwh,rate):
    cost = kwh * rate
    return cost

#this then adds our total usage with our flat fee
def subtotal(cost,fee):
    subtotal = cost + fee
    return subtotal

#main body to get our inputs, and call our functions, then format and print our output
def main():
    kwh = float(input('Enter kWh used: '))
    rate = float(input('Enter rate per kWh: '))
    fee = float(input('Enter service fee: '))

    total = subtotal(calc_cost(kwh,rate),fee)
    print(f'Final bill: {total:.1f}')

if __name__ == '__main__':
    main()

