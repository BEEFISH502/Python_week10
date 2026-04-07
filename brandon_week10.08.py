##8 write a program that calculates how many reps per set
'''
Inputs:
how many sets?

Outputs:
reps for set 1
reps for set 2
reps for set 3

fuunctions:
set_reps(input)
main()

'''

def rep_count(sets):
    reps = []
    for num in sets:
        reps.append(10 + (num * 2))
    return reps

def set_reps():
    set = int(input('How many sets? '))
    sets = []
    for i in range(1, set + 1):
        sets.append(i)
    return sets

def main():
    result = rep_count(set_reps())
    for i, value in enumerate(result):
        print(f'Set {i+1} reps: {value}')


if __name__ == '__main__':
    main()
