# analyze_student_grades.py

import csv

def analyze_csv(file_path, threshold):
    print(f"Students with average grade above {threshold}:\n")
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Assumption: grade field contains comma-separated grades
            grades = list(map(float, row['grade'].split(',')))
            avg_grade = sum(grades) / len(grades)
            if avg_grade > threshold:
                print(f" - {row['name']} (Average Grade: {avg_grade:.2f})")

if __name__ == "__main__":
    csv_file_path = 'students.csv'  # You can change this path
    grade_threshold = 75            # Set threshold
    analyze_csv(csv_file_path, grade_threshold)
