##5. write a program that calculates your parking costs at a garage
'''
Parking parameters:
parking time <2 == $5/hr
parking time >2 == $7/hr

functions:
determine cost(parking time, cost per hour)
calculate cost(time, cost per hour)

main(inputs, output)

'''


def calc(time):
    ##decide what cost per hour is
    if time <= 2:
        cost = 5
    else:
        cost = 5 + 2 * (time - 2)
    return cost

def main():
    ## get our inputs, call functions, print output
    time = int(input('Enter hours parked: '))
    cost = calc(time)
    print(f'Parking cost: {cost}')

if __name__ == '__main__':
    main()



