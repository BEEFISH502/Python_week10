##2. write a program that calculates average scores, and letter grade

'''
Letter Grade Parameters:
A >= 90
B <= 89 and B >=80
C <= 79 and C >= 70
D <= 69 and D >= 60
F <= 59
'''

#inputs will be test scores (score1-3)
#2 outputs Average:, and Letter Grade:
#grade output
def letter_grade(avg):
    if (avg >= 90) and (avg <= 100):
        grade = 'A'
    if (avg >= 80) and (avg <= 89):
        grade = 'B'
    if (avg >= 70) and (avg <=79):
        grade = 'C'
    if (avg >= 60) and (avg <= 69):
        grade = 'D'
    elif avg < 59 and avg >= 0:
        grade = 'F'

    return grade

#average output
def average(scores):
    avg = sum(scores) / len(scores)
    return avg

#main function that gets our inputs, and prints our outputs
def main():
    scores = []
    while len(scores) < 3:
        quiz = len(scores) + 1
        scores.append(float(input(f'Enter quiz {quiz} score: ')))

    avg = average(scores)
    grade = letter_grade(avg)


    print(f'Average: {avg}\nLetter grade: {grade}')
    return scores

if __name__ == '__main__':
    main()

