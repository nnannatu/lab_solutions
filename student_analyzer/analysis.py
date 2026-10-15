"""Analysis helpers: averages, sorting, filtering, decorators, generators."""

from functools import wraps


# ---------- Section 11: Decorator ----------
def logged(func):
    """Decorator that prints when a function is called and what it returns."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] Calling {func.__name__} ...")
        result = func(*args, **kwargs)
        print(f"[log] {func.__name__} returned: {result}")
        return result
    return wrapper


# ---------- Section 11: Generator function ----------
def only_missing(assessments):
    """Yield assessments where mark is None."""
    for a in assessments:
        if a.is_missing():
            yield a


# ---------- Section 11: Iterator class ----------
class CourseIterator:
    """Iterate over assessments belonging to a single course."""

    def __init__(self, assessments, course):
        self._items = [a for a in assessments if a.course.lower() == course.lower()]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item


# ---------- Section 5: math + list methods ----------
@logged
def individual_average(assessments, student_id):
    """Average percentage for one student (ignores missing marks)."""
    percents = [a.percentage for a in assessments
                if a.student_id == student_id and a.percentage is not None]
    if not percents:
        return 0.0
    return round(sum(percents) / len(percents), 2)


@logged
def class_average(assessments):
    """Average percentage across all recorded marks."""
    percents = [a.percentage for a in assessments if a.percentage is not None]
    if not percents:
        return 0.0
    return round(sum(percents) / len(percents), 2)


# ---------- Section 6: sorted / lambda / filter / map ----------
def sort_by_percentage(assessments):
    """Return assessments sorted by percentage, highest first."""
    return sorted(
        [a for a in assessments if a.percentage is not None],
        key=lambda a: a.percentage,
        reverse=True,
    )


def students_below(assessments, threshold=50):
    """Filter: assessments with percentage below the threshold."""
    return list(filter(lambda a: a.percentage is not None and a.percentage < threshold,
                       assessments))


def rounded_percentages(assessments):
    """Map: percentages rounded to whole numbers."""
    return list(map(lambda a: (a.name, a.course, round(a.percentage))
                    if a.percentage is not None else (a.name, a.course, None),
                    assessments))


# ---------- Section 11: Generator expression ----------
def course_names(assessments):
    """Generator expression yielding unique course names."""
    return (name for name in sorted({a.course for a in assessments}))


# ---------- Search helpers ----------
def find_by_student(assessments, query):
    """Case-insensitive search on student name or id."""
    q = query.lower()
    return [a for a in assessments
            if q in a.name.lower() or q in a.student_id.lower()]


def find_by_course(assessments, query):
    q = query.lower()
    return [a for a in assessments if q in a.course.lower()]