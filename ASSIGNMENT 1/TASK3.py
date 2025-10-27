# REVERSE A STRING FUNCTION.

def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]

if __name__ == "__main__":
    # No user input required; use a predefined string and print its reverse.
    s = "AI ASSISTED PROGRAMMIMG USING PYTHON"
    print(reverse_string(s))
    print("String reversed successfully.")
