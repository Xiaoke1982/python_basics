name = input("What is your name?")

#the input() function returns a string
gpa_string = input("What is your GPA?")
gpa = float(gpa_string)

exam1_str = input("What is your exam1 score?")
exam2_str = input("What is your exam2 score?")
exam3_str = input("What is your exam3 score?")

exam1 = float(exam1_str)
exam2 = float(exam2_str)
exam3 = float(exam3_str)

avg = (exam1 + exam2 + exam3) / 3.0

print("Name: ", name)
print("GPA: ", gpa)
print("Your average score: %5.2f" %avg)