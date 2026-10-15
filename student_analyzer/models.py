"""Data classes for the Student Performance Analyzer."""


class Person:
    """Base class. A generic person with a name."""

    def __init__(self, name):
        self.name = name

    def role(self):
        """Polymorphic method — overridden by subclasses."""
        return "person"

    def __str__(self):
        return f"{self.role().capitalize()}: {self.name}"


class Student(Person):
    """A student is a Person with an ID."""

    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def role(self):
        return "student"


class Assessment:
    """A single assessment record for a student in a course."""

    def __init__(self, student_id, name, course, title, mark, max_mark, date):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.title = title
        # mark may be None (missing work)
        self.mark = mark
        self.max_mark = max_mark
        self.date = date

    @property
    def percentage(self):
        """Return the percentage or None if missing."""
        if self.mark is None or self.max_mark == 0:
            return None
        return round((self.mark / self.max_mark) * 100, 2)

    def is_missing(self):
        return self.mark is None

    def __str__(self):
        mark_display = "MISSING" if self.is_missing() else f"{self.mark}/{self.max_mark}"
        return f"[{self.student_id}] {self.name} — {self.course} {self.title}: {mark_display}"

    def to_dict(self):
        """Convert to a plain dict (used by storage when saving)."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "course": self.course,
            "assessment": self.title,
            "mark": "" if self.mark is None else self.mark,
            "max_mark": self.max_mark,
            "date": self.date,
        }