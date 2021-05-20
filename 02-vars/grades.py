homework = float(input("Homework Grade: "))
labs = float(input("Labs Grade: "))
test1 = float(input("Test 1 Grade: "))
test2 = float(input("Test 2 Grade: "))
test3 = float(input("Test 3 Grade: "))

final_grade = homework * .2 + labs * .5 + test1 * .1 + test2 * .1 + test3 * .1

print(f"Final Grade {round(final_grade)}.")