#4. Write a program that cleans up a name and creates a username
'''
Inputs
1.first name
2. last name

output
1.clean name
  1a. username

functions:
1. clean_name(first,last)
2. username(clean_name)

'''

def clean_name(first, last):
    #strip and lower our inputs
    clean_first = first.strip().lower()
    clean_last = last.strip().lower()
    return clean_first, clean_last

def username(clean_first,clean_last):
    #concatenate clean names with a period
    user = clean_first + '.' + clean_last
    return user

def main():
    ## get our inputs, format, then print
    first = input('Enter first name: ')
    last = input('Enter last name: ')


    clean_first, clean_last = clean_name(first, last)
    name2 = username(clean_first,clean_last)
    print(f'Username: {name2}')


if __name__ == '__main__':
    main()
