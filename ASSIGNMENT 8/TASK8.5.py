# TASK 8.5: Date Format Conversion
from datetime import datetime
from typing import Iterable, Tuple, Union


def convert_date_format(date_str: str) -> str:
    """
    Convert a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY'.

    Raises ValueError for invalid formats or impossible dates.
    """
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string in 'YYYY-MM-DD' format")

    # Enforce exact format with zero-padding using datetime.
    try:
        parsed = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(f"Invalid date format: {date_str}") from exc

    return parsed.strftime("%d-%m-%Y")


def _run_tests() -> None:
    """Run AI-generated tests for convert_date_format."""
    print("Running convert_date_format tests...")

    valid_cases: Iterable[Tuple[str, str]] = [
        ("2023-10-15", "15-10-2023"),
        ("1999-01-01", "01-01-1999"),
        ("2000-02-29", "29-02-2000"),  # leap year
        ("2024-12-31", "31-12-2024"),
        ("1985-07-04", "04-07-1985"),
        ("2020-11-09", "09-11-2020"),
    ]

    for input_date, expected in valid_cases:
        result = convert_date_format(input_date)
        print(f"{input_date} -> {result}")
        assert result == expected, f"Expected {expected} but got {result}"

    invalid_cases: Iterable[Union[str, object]] = [
        "2023/10/15",   # wrong separator
        "15-10-2023",   # wrong order
        "2023-13-01",   # invalid month
        "2023-00-10",   # month zero
        "2023-11-31",   # invalid day
        "2023-2-05",    # missing zero padding
        "",             # empty string
        None,           # non-string
        20231015,       # non-string numeric
    ]

    for bad_input in invalid_cases:
        try:
            convert_date_format(bad_input)  # type: ignore[arg-type]
            print(f"WARNING: Invalid input did not raise error: {bad_input!r}")
        except (ValueError, TypeError):
            print(f"Invalid input correctly raised error: {bad_input!r}")

    print("All test cases passed")


if __name__ == "__main__":
    _run_tests()
    print("Function converts input format correctly for all test cases")

