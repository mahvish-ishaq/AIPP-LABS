# TASK 8.2: Grade Assignment (Loops)

from math import isnan


def assign_grade(score):
    """
    Returns the letter grade for a numeric score using these rules:
    90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    Invalid inputs (non-number, NaN, or outside 0..100) raise ValueError.
    """
    # Type and value validation
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise ValueError("Score must be a number")
    if isnan(score):
        raise ValueError("Score cannot be NaN")
    if score < 0 or score > 100:
        raise ValueError("Score must be in the range 0..100")

    # Grade boundaries
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def _run_tests():
    # Boundary and representative valid scores
    valid_cases = [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
        (95.5, "A"),
        (84.9, "B"),
        (74.0, "C"),
        (61.2, "D"),
        (12.3, "F"),
    ]

    for score, expected in valid_cases:
        assert assign_grade(score) == expected, f"Expected {expected} for {score}"

    # Invalid inputs
    invalid_scores = [-5, 105, "eighty", None, float("nan")]
    for bad in invalid_scores:
        ok = False
        try:
            assign_grade(bad)
        except ValueError:
            ok = True
        assert ok, f"Expected ValueError for invalid score: {bad!r}"


if __name__ == "__main__":
    _run_tests()
    print("Grade assignment function passing test suite")
