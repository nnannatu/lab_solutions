"""File storage and validation utilities."""

import csv
import re
from pathlib import Path

from models import Assessment

DATA_FILE = Path("data/students.csv")

# Regex patterns (Syllabus Section 7)
NAME_PATTERN = re.compile(r"[A-Za-z][A-Za-z .'-]{1,49}")
ID_PATTERN = re.compile(r"S\d{3}")
DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")


def valid_name(name):
    """Full-match a name: letters, spaces, dots, hyphens, apostrophes."""
    return re.fullmatch(NAME_PATTERN, name) is not None


def valid_student_id(sid):
    """Full-match an ID like S001, S042, ..."""
    return re.fullmatch(ID_PATTERN, sid) is not None


def valid_date(date_str):
    """Full-match a date like 2025-09-10."""
    return re.fullmatch(DATE_PATTERN, date_str) is not None


def load_assessments(path=DATA_FILE):
    """Load assessments from CSV. Demonstrates try/except/else/finally."""
    assessments = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                mark_raw = row["mark"].strip()
                mark = None if mark_raw == "" else int(mark_raw)
                assessments.append(
                    Assessment(
                        student_id=row["student_id"],
                        name=row["name"],
                        course=row["course"],
                        title=row["assessment"],
                        mark=mark,
                        max_mark=int(row["max_mark"]),
                        date=row["date"],
                    )
                )
    except FileNotFoundError:
        print(f"[warn] No file at {path}. Starting with an empty list.")
    except (ValueError, KeyError) as exc:
        print(f"[error] Malformed row in CSV: {exc}")
    else:
        print(f"[ok] Loaded {len(assessments)} assessment records.")
    finally:
        print("[info] Load attempt finished.\n")
    return assessments


def save_assessments(assessments, path=DATA_FILE):
    """Save assessments to CSV using a context manager."""
    fieldnames = ["student_id", "name", "course", "assessment", "mark", "max_mark", "date"]
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for a in assessments:
                writer.writerow(a.to_dict())
    except OSError as exc:
        print(f"[error] Could not save: {exc}")
    else:
        print(f"[ok] Saved {len(assessments)} records to {path}.")


def read_lines(path=DATA_FILE):
    """Iterator demo (Section 11): yields file lines one at a time."""
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                yield line.rstrip("\n")
    except FileNotFoundError:
        return