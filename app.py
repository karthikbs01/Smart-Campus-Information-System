"""
Smart Campus Information System
Main Application - Lab 9 (Integration of Labs 1 to 8)
"""

import os

# LAB 1: Student Registration and Grade Evaluation

def student_registration():
    print("\n=== Student Registration and Grade Evaluation ===")
    student_name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))

    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)
    print("Performance Remark:", remark)



# LAB 2: Course Enrollment Management

def course_enrollment():
    print("\n=== Course Enrollment Management System ===")
    courses = []
    max_courses = 5

    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")
        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue

        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue

        courses.append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.")

    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")
    print("Total courses enrolled:", len(courses))


# LAB 3: Student Record Data Management
def student_records():
    print("\n=== Student Record Data Management ===")

    students = []
    students.append({"name": "Priya",  "age": 20, "grades": [85, 90, 78]})
    students.append({"name": "Rahul",  "age": 21, "grades": [72, 88, 91]})
    students.append({"name": "Anita",  "age": 19, "grades": [95, 89, 92]})

    print("\n--- Student Records ---")
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grades:", student["grades"])
        print("-----------------------")

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    print("\n--- Event Participation Analysis ---")
    print("Common Participants:", event_A & event_B)
    print("All Participants:", event_A | event_B)
    print("Only Event A Participants:", event_A - event_B)


# LAB 4: Sorting and Searching Student IDs
def search_sort_students():
    print("\n=== Sorting and Searching Student IDs ===")

    student_ids = [105, 102, 110, 108, 101, 115]
    print("Original IDs:", student_ids)

    # Bubble Sort
    ids_bubble = student_ids[:]
    n = len(ids_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ids_bubble[j] > ids_bubble[j + 1]:
                ids_bubble[j], ids_bubble[j + 1] = ids_bubble[j + 1], ids_bubble[j]
    print("Sorted IDs (Bubble Sort):", ids_bubble)

    # Selection Sort
    ids_selection = student_ids[:]
    n = len(ids_selection)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if ids_selection[j] < ids_selection[min_index]:
                min_index = j
        ids_selection[i], ids_selection[min_index] = ids_selection[min_index], ids_selection[i]
    print("Sorted IDs (Selection Sort):", ids_selection)

    target = int(input("Enter student ID to search: "))

    # Linear Search
    found_index = -1
    for i in range(len(ids_bubble)):
        if ids_bubble[i] == target:
            found_index = i
            break
    if found_index != -1:
        print(f"Linear Search: ID {target} found at index {found_index}")
    else:
        print("Linear Search: ID not found")

    # Binary Search
    low, high, found_index = 0, len(ids_bubble) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if ids_bubble[mid] == target:
            found_index = mid
            break
        elif ids_bubble[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if found_index != -1:
        print(f"Binary Search: ID {target} found at index {found_index}")
    else:
        print("Binary Search: ID not found")


# LAB 5: Fee Calculation using Functions
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee

def fee_calculation():
    print("\n=== Student Fee Calculation ===")
    tuition = float(input("Enter tuition fee: "))
    hostel_input = input("Enter hostel fee (press Enter to skip): ")
    transport_input = input("Enter transportation fee (press Enter to skip): ")

    hostel = float(hostel_input) if hostel_input.strip() else 0
    transport = float(transport_input) if transport_input.strip() else 0

    total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
    print(f"\nTuition Fee     : {tuition}")
    print(f"Hostel Fee      : {hostel}")
    print(f"Transport Fee   : {transport}")
    print(f"Total Fee       : {total}")


# LAB 6: File Handling for Academic Records
def file_management():
    print("\n=== File Handling for Student Academic Records ===")
    filename = "student_records.txt"

    # Write records
    with open(filename, "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print("Student records written to file successfully.")

    # Read records
    print("\nReading stored records:")
    with open(filename, "r") as file:
        records = file.readlines()
    for record in records:
        print(record.strip())

    # Generate report
    print("\nGenerating Report:")
    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:
        parts = record.strip().split(",")
        marks = int(parts[2])
        total_students += 1
        total_marks += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student = parts[1]

    print("Total Students:", total_students)
    print("Average Marks:", total_marks / total_students)
    print(f"Top Student: {top_student} with {highest_marks} marks")


# LAB 7: Directory Scanning with Exception Handling
class MissingFileOrFolderError(Exception):
    pass

def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")

        print(f"\nScanning directory: {path}\n")
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                print(f"{sub_indent}{f}")
            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder detected: {root}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def directory_scanner():
    print("\n=== Directory Scanning ===")
    path = input("Enter the directory path to scan: ")
    scan_directory(path)


# ─────────────────────────────────────────────
# LAB 8: Performance Analytics (NumPy, Pandas, Matplotlib)
# ─────────────────────────────────────────────
def performance_analytics():
    print("\n=== Student Performance Analytics ===")
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"Required library not installed: {e}")
        print("Install using: pip install numpy pandas matplotlib")
        return

    csv_file = "student_performance.csv"

    # Create sample CSV if it doesn't exist
    if not os.path.exists(csv_file):
        sample_data = "Name,Math,Science,English\nPriya,88,92,85\nRahul,75,80,70\nAnita,95,89,93\nKiran,60,72,65\n"
        with open(csv_file, "w") as f:
            f.write(sample_data)
        print(f"Sample '{csv_file}' created.")

    try:
        df = pd.read_csv(csv_file)
        print("\n--- Raw Data ---")
        print(df.head())

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy()
        mean_scores   = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)

        print("\n--- NumPy Analysis ---")
        print(f"Mean   (Math, Science, English): {mean_scores}")
        print(f"Median (Math, Science, English): {median_scores}")
        print(f"Std Dev(Math, Science, English): {std_dev_scores}")

        print("\n--- Top Performers ---")
        print("Math   :", df.loc[df["Math"].idxmax(), "Name"])
        print("Science:", df.loc[df["Science"].idxmax(), "Name"])
        print("English:", df.loc[df["English"].idxmax(), "Name"])

        # Charts
        subjects = ["Math", "Science", "English"]
        plt.figure()
        plt.bar(subjects, mean_scores, color=["blue", "green", "red"])
        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.savefig("avg_scores.png")
        print("\nChart saved as avg_scores.png")

        df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")
        plt.tight_layout()
        plt.savefig("student_performance.png")
        print("Chart saved as student_performance.png")

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# ─────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────
def main():
    menu = {
        "1": ("Student Registration & Grade Evaluation", student_registration),
        "2": ("Course Enrollment Management",            course_enrollment),
        "3": ("Student Record Data Management",          student_records),
        "4": ("Sorting and Searching Student IDs",       search_sort_students),
        "5": ("Fee Calculation",                         fee_calculation),
        "6": ("File Handling for Academic Records",      file_management),
        "7": ("Directory Scanning",                      directory_scanner),
        "8": ("Performance Analytics",                   performance_analytics),
        "0": ("Exit",                                    None),
    }

    while True:
        print("\n" + "=" * 50)
        print("   SMART CAMPUS INFORMATION SYSTEM")
        print("=" * 50)
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Exiting Smart Campus Information System. Goodbye!")
            break
        elif choice in menu:
            _, func = menu[choice]
            func()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
