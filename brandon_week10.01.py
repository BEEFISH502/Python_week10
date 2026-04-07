#1. write a program that performs checkout totals
##Use two functions
# this will handle our initial value; takes out input p1, q1 etc. and pairs them to get total price per item type
def values(q1, p1, q2, p2):
    item1 = q1 * p1
    item2 = q2 * p2
    return item1, item2
## this will calculate our full subtotal
def totals(item1, item2):
    subtotal = item1 + item2
    return subtotal
## main body to get our inputs, and call our other two functions and print.
def main():
    p1 = float(input('Enter item 1 price: '))
    q1 = int(input('Enter item 1 quantity: '))
    p2 = float(input('Enter item 2 price: '))
    q2 = int(input('Enter item 2 quantity: '))

    item1, item2 = values(q1, p1, q2, p2)
    subtotal = totals(item1, item2)


    print(f'Subtotal: {subtotal}')

'''not necesary for this project but i learned this keeps code from being unintentionally executed,
which allows the modules to be used for seperate projects without running the main function'''
if __name__ == '__main__':
    main()

