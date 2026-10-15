"""Small demos for syllabus points that don't fit neatly in the main app.

Run with:  python syllabus_demo.py
"""

from models import Person, Student


# ---------- Section 1-4: == vs is ----------
def equality_vs_identity():
    print("=== == vs is ===")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a == b -> {a == b}   (same contents)")
    print(f"a is b -> {a is b}   (different objects)")
    print(f"a == c -> {a == c}")
    print(f"a is c -> {a is c}   (same object)")
    # Why it matters: use == to compare values, is to compare identity (None, True, False)
    x = None
    print(f"x is None -> {x is None}   (correct)")
    print()


# ---------- Section 5: Recursion ----------
def total_marks(assessments, index=0):
    """Recursively sum all non-missing marks."""
    if index >= len(assessments):
        return 0
    current = assessments[index].mark or 0
    return current + total_marks(assessments, index + 1)


def count_missing(assessments, index=0):
    """Recursively count missing assessments."""
    if index >= len(assessments):
        return 0
    here = 1 if assessments[index].is_missing() else 0
    return here + count_missing(assessments, index + 1)


# ---------- Section 10: Inheritance and polymorphism ----------
def polymorphism_demo():
    print("=== Inheritance & Polymorphism ===")
    people = [Person("Dr. Ada"), Student("Alice Johnson", "S001")]
    for p in people:
        print(" ", p, "->", p.role())
    print()


# ---------- Section 7: regex showcase ----------
def regex_demo():
    import re
    print("=== Regex demo (Section 7) ===")
    text = "Student S001 and student S002 are enrolled. S003 is absent."
    print("re.search   :", re.search(r"S\d{3}", text).group())
    print("re.match    :", re.match(r"Student", text) is not None)
    print("re.fullmatch:", re.fullmatch(r"S\d{3}", "S042") is not None)
    print("re.findall  :", re.findall(r"S\d{3}", text))
    print()


if __name__ == "__main__":
    equality_vs_identity()
    polymorphism_demo()
    regex_demo()

    # A tiny in-memory dataset to show recursion without loading the file
    from models import Assessment

    sample = [
        Assessment("S001", "Alice", "Math", "Quiz 1", 18, 20, "2025-09-10"),
        Assessment("S002", "Bob", "Math", "Quiz 1", None, 20, "2025-09-10"),
        Assessment("S003", "Carla", "Math", "Quiz 1", 20, 20, "2025-09-10"),
    ]
    print("Total marks (recursion)   :", total_marks(sample))
    print("Missing count (recursion) :", count_missing(sample))