def grade_it(score):
    if marks>40:
        return "Pass"
    else:
        return "Fail"
marks = [36, 10, 67, 89, 76]
results = [grade_it(score) for score in marks]
print(results)