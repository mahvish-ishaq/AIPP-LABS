# TASK 8.1: Email Validation Logic
import re

def is_valid_email(email: str) -> bool:
    """
    Validates an email string based on the given requirements:
    - Must contain exactly one '@' and at least one '.' in the domain part
    - Must not start or end with special characters (non-alphanumeric)
    - Should not allow multiple '@'
    Additional pragmatic checks:
    - No consecutive dots
    - Domain labels do not start or end with hyphen or dot
    """
    if not isinstance(email, str) or not email:
        return False

    # Must contain exactly one '@'
    if email.count("@") != 1:
        return False

    local, domain = email.split("@", 1)

    # Must contain '.' somewhere in the domain
    if "." not in domain:
        return False

    # Must not start or end with special characters (non-alphanumeric)
    if not email[0].isalnum() or not email[-1].isalnum():
        return False

    # No consecutive dots anywhere
    if ".." in email:
        return False

    # Local part: allow alnum and . _ + -
    local_allowed = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._+-]*[A-Za-z0-9])?$")
    if not local_allowed.fullmatch(local):
        return False

    # Domain part: labels separated by dots, alnum and hyphen within labels
    domain_labels = domain.split(".")
    if any(len(label) == 0 for label in domain_labels):
        return False
    for label in domain_labels:
        # label must start and end with alphanumeric, hyphens allowed inside
        if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?", label):
            return False

    # Final TLD should have at least 2 letters (common constraint)
    if not re.fullmatch(r"[A-Za-z]{2,}", domain_labels[-1]):
        return False

    return True


def _run_tests() -> None:
    # Valid cases
    valid_emails = [
        "user@example.com",
        "first.last@sub.domain.co",
        "u1+tag@ex-ample.co.in",
        "name_surname@domain.org",
        "abc123@xyz123.io",
    ]

    # Invalid cases
    invalid_emails = [
        "userexample.com",         # missing @
        "user@@example.com",       # multiple @
        ".user@example.com",       # starts with special
        "user.@example.com",       # local ends with special
        "user@.example.com",       # domain starts with special
        "user@example.com.",       # ends with special
        "user@example",            # no dot in domain
        "user@exam..ple.com",      # consecutive dots
        "user@-example.com",       # domain label starts with hyphen
        "user@example-.com",       # domain label ends with hyphen
        "user@ex_ample.com",       # underscore not allowed in domain
        "",                        # empty
        12345,                     # not a string
    ]

    for e in valid_emails:
        assert is_valid_email(e) is True, f"Expected valid: {e}"

    for e in invalid_emails:
        assert is_valid_email(e) is False, f"Expected invalid: {e}"


if __name__ == "__main__":
    _run_tests()
    print("Email validation logic passing all test cases")

