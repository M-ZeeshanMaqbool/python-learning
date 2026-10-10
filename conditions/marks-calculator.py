
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

total_percentage = (marks1 + marks2 + marks3) / 3

if total_percentage > 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You have passed!")
else:
    print("You have failed!")
