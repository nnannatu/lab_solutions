"""Student Performance Analyzer — command-line application."""

import sys

import analysis
import reporting
import storage
from models import Assessment


# ---------- Section 1–4: == vs is demo happens in syllabus_demo.py ----------

def menu():
    print("""
========= Student Performance Analyzer =========
  1. Add assessment record
  2. View all records
  3. Search by student
  4. Search by course
  5. Show class summary (pandas)
  6. Show NumPy statistics
  7. Flag missing work
  8. Individual student average
  9. Save to file
 10. Export summary report
  0. Exit
===============================================
""")


def prompt(text):
    return input(text).strip()


def add_record(assessments):
    """Prompt user to add a new assessment (Section 9: input validation)."""
    try:
        sid = prompt("Student ID (e.g. S007): ").upper()
        if not storage.valid_student_id(sid):
            raise ValueError("Invalid student ID. Must look like S001.")

        name = prompt("Student name: ")
        if not storage.valid_name(name):
            raise ValueError("Invalid name. Letters, spaces, dots, hyphens, apostrophes.")

        course = prompt("Course: ")
        if not course:
            raise ValueError("Course cannot be empty.")

        title = prompt("Assessment title: ")
        if not title:
            raise ValueError("Title cannot be empty.")

        mark_raw = prompt("Mark (leave blank if missing): ")
        max_raw = prompt("Max mark: ")
        date = prompt("Date (YYYY-MM-DD): ")
        if not storage.valid_date(date):
            raise ValueError("Invalid date. Use YYYY-MM-DD.")

        max_mark = int(max_raw)
        if max_mark <= 0:
            raise ValueError("Max mark must be greater than zero.")

        if mark_raw == "":
            mark = None
        else:
            mark = int(mark_raw)
            if mark < 0 or mark > max_mark:
                raise ValueError("Mark must be between 0 and max mark.")

        assessments.append(
            Assessment(sid, name, course, title, mark, max_mark, date)
        )
    except ValueError as exc:
        print(f"[error] {exc}")
    else:
        print("[ok] Record added.")
    finally:
        print("[info] Add operation finished.\n")


def show_records(assessments):
    if not assessments:
        print("No records yet.")
        return
    print("\n--- All Assessment Records ---")
    for a in assessments:
        print(" ", a)
    print()


def search_student(assessments):
    q = prompt("Enter student name or ID: ")
    results = analysis.find_by_student(assessments, q)
    if not results:
        print("No matches.")
        return
    for a in results:
        print(" ", a)


def search_course(assessments):
    q = prompt("Enter course name: ")
    results = analysis.find_by_course(assessments, q)
    if not results:
        print("No matches.")
        return
    for a in results:
        print(" ", a)


def flag_missing(assessments):
    print("\n--- Missing Work ---")
    found = False
    for a in analysis.only_missing(assessments):   # generator
        found = True
        print(" ", a)
    if not found:
        print("  None — well done!")


def show_individual_average(assessments):
    sid = prompt("Student ID: ").upper()
    avg = analysis.individual_average(assessments, sid)
    print(f"Average for {sid}: {avg}%")


def main():
    print("Starting Student Performance Analyzer ...")
    assessments = storage.load_assessments()

    while True:
        menu()
        choice = prompt("Choose an option: ")

        if choice == "1":
            add_record(assessments)
        elif choice == "2":
            show_records(assessments)
        elif choice == "3":
            search_student(assessments)
        elif choice == "4":
            search_course(assessments)
        elif choice == "5":
            reporting.print_summary_table(assessments)
        elif choice == "6":
            reporting.numpy_stats(assessments)
        elif choice == "7":
            flag_missing(assessments)
        elif choice == "8":
            show_individual_average(assessments)
        elif choice == "9":
            storage.save_assessments(assessments)
        elif choice == "10":
            reporting.export_summary_csv(assessments)
        elif choice == "0":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("[warn] Invalid option. Try again.\n")


if __name__ == "__main__":
    main()