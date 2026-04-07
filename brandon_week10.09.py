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
def percent(students, A):
    percent_A = ( A / students ) * 100

def main():
    students = int(input('Enter total number of students: '))
    A = int(input('Enter number choosing Option A: '))

    total = percent(students, A)
    print(f'Option A percent: {total:.1f}')

main()




