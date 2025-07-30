# Write a function analyze_scores(*scores, **student_info) that:
# 	1.	Accepts multiple test scores as *args and student details like name, roll, class etc. as **kwargs.
# 	2.	Filters the scores to keep only values ≥ 40 (passing marks).
# 	3.	Calculates:
# 	•	Total marks using reduce()
# 	•	Average marks using map() + lambda
# 	4.	Handles:
# 	•	Empty scores (use try-except)
# 	5.	Uses the walrus operator when reading input dynamically from a user.


# Solution

from functools import reduce

def analyze_scores(*scores, **student_info):
    # Display student information
    print("\n📘 Student Info:")
    for key, value in student_info.items():
        print(f"  {key.capitalize()} : {value}")

    try:
        # Step 1: Filter scores ≥ 40 (passing marks)
        passing_scores = list(filter(lambda x: x >= 40, scores))
        print("\n Passing Scores:", passing_scores)

        if not passing_scores:
            print("No passing scores found.")
            return

        # Step 2: Calculate total using reduce
        total = reduce(lambda x, y: x + y, passing_scores)
        print(" Total Marks:", total)

        # Step 3: Calculate average
        average = total / len(passing_scores)
        print(" Average Marks:", average)

    except Exception as e:
        print("❌ Error:", e)


#  Collect scores from user using walrus operator
print(" Enter scores for the student (type 'q' to quit):")
scores = []
while (val := input("Enter a score (or 'q' to quit): ")) != 'q':
    try:
        scores.append(int(val))
    except:
        print("❌ Invalid input. Please enter a number.")

#  Call the function with *args and **kwargs
analyze_scores(*scores, name="Debadrita", roll=22, branch="CSE")