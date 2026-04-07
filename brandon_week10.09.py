##9 write a program for a simple survey summary.
'''
Inputs:
How many total students: 20
how many choose option A: 7

outputs:
percentage of choice A
percentage of all other choices

functions:
main()
percent calculater ((part/whole) *100)

'''
def percent(part,whole):
    return (part/whole) * 100

def main():
    whole = int(input(f'Enter total students: '))
    part = int(input(f'Enter number choosing Option A: '))

    percent_A = percent(part,whole)
    print(f'Option A percent: {percent_A}')

if __name__ == '__main__':
    main()







