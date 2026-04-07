def fuel_cost(miles,mpg,price_per_gallon):
    gallons = miles / mpg
    return gallons * price_per_gallon

def trip_total(fuel_cost,food_budget):
    return fuel_cost + food_budget

def main():
    miles = float(input('Enter miles to drive: '))
    mpg = float(input('Enter miles per gallon: '))
    price_per_gallon = float(input('Enter gas price per gallon: '))
    food_budget = float(input('Enter food budget: '))

    fuel = fuel_cost(miles,mpg,price_per_gallon)
    total = trip_total(fuel,food_budget)
    print(f'Total trip cost: {total:.1f}')

if __name__ == '__main__':
    main()
