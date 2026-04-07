##6. write a program that calculates the min and max temps in a list
'''
Functions:
1. update_min()
2. update_max()

Input:
temperature

output:
min_temp
max_temp

'''
## always update our minimum
def update_min(temps):
    min_temp = min(temps)
    return min_temp

## always update our maximum
def update_max(temps):
    max_temp = max(temps)
    return max_temp

## define inputs, call functions, format and output
def main():
    temp = int(input('How many temperatures? '))
    temps = []

    for i in range(temp):
        temps.append(float(input(f'Enter temperature {i+1}: ')))
    min_temp = update_min(temps)
    max_temp = update_max(temps)
    print(f'Minimum: {min_temp}\nMaximum: {max_temp}')

    return temps

if __name__ == '__main__':
    main()



