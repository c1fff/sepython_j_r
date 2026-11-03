### Assignment recapApp ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO
# Implement a console-based Student Grades Manager.
# The program reads data from a CSV file, allows some data processing and summary operations, and writes results back to another file.

import csv
from pathlib import Path

# ================================
# Task 1: File Reading
# ================================

def read_grades(filename):
    """
    Reads the CSV file and returns a list of tuples (student_id, name, grade).
    Handles file-not-found gracefully: Log the error to the console and return an empty list.
    """
    try:
        with open(filename, newline="") as f:
            return [(int(i), n, int(g)) for i, n, g in csv.reader(f, delimiter=";")]
    except FileNotFoundError as e:
        print(e)
        return []


# ================================
# Task 2: Filtering and Transformations
# the parameter 'students' is a list
# ================================

def filter_passing(students):
    """
    Filters and returns students with grade >= 60.
    """
    return [s for s in students if s[2] >= 60]

def to_name_grade_dict(students):
    """
    Converts list of tuples to a dictionary {name: grade}.
    """
    return {n: g for _, n, g in students}

def curve_grades(students, curve_by):
    """
    Returns a new list of tuples with grades increased by curve_by (max 100).
    """
    return [(i, n, min(100, g + curve_by)) for i, n, g in students]


# ================================
# Task 3: Summary Statistics
# ================================

def print_statistics(students):
    """
    Prints number of students, average grade, min, and max. Use the formatting in the example:
    Example:
    Number of students: 5
    Average grade: 82.6
    Lowest grade: 59 (David)
    Highest grade: 100 (Eve)

    """
    print(f"Number of students: {len(students)}")
    if students:
        ordered = sorted(students, key=lambda s: s[2])
        print(f"Average grade: {sum(s[2] for s in students) / len(students):.1f}")
        for label, s in (("Lowest", ordered[0]), ("Highest", ordered[-1])):
            print(f"{label} grade: {s[2]} ({s[1]})")


# ================================
# Task 4: File Writing
# ================================

def write_grades(filename, students):
    """
    Writes the list of student tuples back to a CSV file.
    Sort by name before writing.
    """
    with open(filename, "w", newline="") as f:
        csv.writer(f, delimiter=";").writerows(sorted(students, key=lambda s: s[1]))


# ================================
# Task 5: Putting It All Together
# ================================

def main():
    # Program flow:
    # 1. Read file
    # 2. Print stats
    # 3. Filter failing
    # 4. Curve grades +5
    # 5. Print stats again
    # 6. Write curved grades
    students = read_grades(Path(__file__).with_name("grades.csv"))
    print_statistics(students)
    students = curve_grades(filter_passing(students), 5)
    print_statistics(students)
    write_grades(Path(__file__).with_name("curved_grades.csv"), students)


if __name__ == "__main__":
    main()
  

