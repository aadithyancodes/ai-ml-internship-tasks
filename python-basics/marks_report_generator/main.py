def generate_report(marks):
    return [sum(marks)/len(marks), max(marks), min(marks)]
marks = [10, 20, 30, 40]
result = generate_report(marks)
print("Average Marks = ",result[0])
print("Maximum Marks = ",result[1])
print("Minimum Marks = ",result[2])



"""def generate_report(marks):
    total=0
    for score in marks:
        total=total+score
    return [total/len(marks), max(marks), min(marks)]
marks = [10, 20, 30, 50]
result = generate_report(marks)
print("Average Marks = ",result[0])
print("Maximum Marks = ",result[1])
print("Minimum Marks = ",result[2])
"""