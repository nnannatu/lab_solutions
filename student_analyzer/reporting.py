"""Tabular reports using pandas and NumPy."""

import numpy as np
import pandas as pd

from models import Assessment


def _to_dataframe(assessments):
    rows = [a.to_dict() for a in assessments]
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["mark"] = pd.to_numeric(df["mark"], errors="coerce")
    df["max_mark"] = pd.to_numeric(df["max_mark"], errors="coerce")
    df["percentage"] = (df["mark"] / df["max_mark"] * 100).round(2)
    return df


def summary_table(assessments):
    """Per-student summary as a pandas DataFrame."""
    df = _to_dataframe(assessments)
    if df.empty:
        print("No data to summarize.")
        return None

    summary = (
        df.groupby(["student_id", "name"])
        .agg(
            assessments=("assessment", "count"),
            recorded=("percentage", lambda s: s.notna().sum()),
            missing=("percentage", lambda s: s.isna().sum()),
            avg_percentage=("percentage", "mean"),
            best=("percentage", "max"),
        )
        .round(2)
        .reset_index()
    )
    return summary


def print_summary_table(assessments):
    summary = summary_table(assessments)
    if summary is not None:
        print("\n=== Class Summary (pandas) ===")
        print(summary.to_string(index=False))
        print()


def numpy_stats(assessments):
    """NumPy calculation on all recorded percentages."""
    values = np.array([a.percentage for a in assessments
                       if a.percentage is not None], dtype=float)
    if values.size == 0:
        print("No recorded marks for NumPy stats.")
        return None
    stats = {
        "count": int(values.size),
        "mean": round(float(np.mean(values)), 2),
        "median": round(float(np.median(values)), 2),
        "std_dev": round(float(np.std(values)), 2),
        "min": round(float(np.min(values)), 2),
        "max": round(float(np.max(values)), 2),
    }
    print("\n=== NumPy Statistics ===")
    for k, v in stats.items():
        print(f"  {k:>8}: {v}")
    print()
    return stats


def export_summary_csv(assessments, path="data/summary.csv"):
    """Export the pandas summary to a CSV."""
    summary = summary_table(assessments)
    if summary is None:
        return
    summary.to_csv(path, index=False)
    print(f"[ok] Summary exported to {path}.")