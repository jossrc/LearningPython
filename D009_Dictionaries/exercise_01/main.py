student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇

def set_grades(student_score):
    if student_score < 70:
        return "Fail"
    elif student_score < 80:
        return "Acceptable"
    elif student_score < 90:
        return "Exceeds Expectations"
    else:
        return "Outstanding"


for name, score in student_scores.items():
    student_grades[name] = set_grades(score)


# 🚨 Don't change the code below 👇
print(student_grades)
