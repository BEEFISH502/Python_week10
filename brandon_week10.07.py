## write a program that calculates bussiness order with discount applied
'''
Functions:
apply_discount()
applu_tax()

inputs:
total bill
discount percent
tax percent

output:
total bill
'''

def apply_tax(discounted,tax):
    ##calculate taxes after discount applied
    taxes =  (discounted * tax)
    return taxes

def apply_discount(bill,discount):
    #apply discount to total bill
    discounted = bill - (bill * discount)
    return discounted

def main():
    ##define inputs, format percentages, call functions, print formatted output
    bill = float(input('Enter subtotal: '))
    discount = float(input('Enter discount percent: '))
    tax = float(input('Enter tax rate percent: '))

    discount = discount / 100
    tax = tax / 100

    discounted = apply_discount(bill,discount)
    taxes = apply_tax(discounted,tax)
    subtotal = taxes + discounted
    print(f'Final total: {subtotal:.1f}')

if __name__ == '__main__':
    main()