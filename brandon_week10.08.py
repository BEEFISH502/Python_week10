##8 write a program that calculates how many reps per set
'''
Inputs:
how many sets?

Outputs:
reps for set 1
reps for set 2
reps for set 3

fuunctions:
rep_calc(input)
main()

'''
def rep_calc():
    sets = ['1','2','3']
    reps_list = [int(num) for num in sets]
    reps = []
    for i in range(len(reps_list)):
        reps.append(10 + ((2 * i)+ 2))
    return reps

def main():
    count = int(input('Enter number of sets: '))
    sets = []
    for i in range(1, count +1):
        sets.append(str(i))
    reps = rep_calc()
    for i in range(len(reps)):
        print(f'Set {sets[i]} reps: {reps[i]}')

main()
