import math
def gradingStudents(grades):
    for index,grade in enumerate(grades):
        if grade < 38:
            continue
        next_mult = math.ceil(grade/5)*5
        if next_mult - grade < 3:
            grades[index] = next_mult
    return grades

result = gradingStudents([73,67,38,33])
print(result)
