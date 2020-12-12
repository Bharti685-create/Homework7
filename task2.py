
grade_letter = ''
grade_marks = 0.0

def get_student_grades(score):

    if score >= 90:
        grade_letter = 'A'
        grade_marks = 4.0
    elif score >= 80:
        grade_letter = 'B'
        grade_marks = 3.0
    elif score >= 70:
        grade_letter = 'C'
        grade_marks = 2.0
    elif score >= 60:
        grade_letter = 'D'
        grade_marks = 1.0
    elif score < 60:
        grade_letter = 'F'
        grade_marks = 0.0
    return grade_marks

def main():
    import pandas as pd

    READ_FILENAME = 'scores.csv'

    df_scores = pd.read_csv(READ_FILENAME, delimiter=',', index_col=0, header=0)
    df_student_grades = df_scores.applymap(get_student_grades)
    pd.set_option('precision', 2)

    mean = df_student_grades.mean(axis = 0)
    print(mean)

    gpa = df_student_grades.stack().mean()
    print(f'The class GPA is {gpa:.2f}')

main()

