'''TASK 2'''
 # COMPARE GEMINI AND COPILOT OUTPUTS FOR PALINDROME CHECK FUNCTION.
 # COPILOT VERSION.
def is_palindrome(s: str, *, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool:
    """
    Return True if s is a palindrome.
    By default, comparison is case-insensitive and non-alphanumeric characters are ignored.
    Examples:
      is_palindrome("Racecar") -> True
      is_palindrome("A man, a plan, a canal: Panama") -> True
    """
    if ignore_non_alnum:
        filtered = ''.join(ch for ch in s if ch.isalnum())
    else:
        filtered = s
    if ignore_case:
        filtered = filtered.lower()
    return filtered == filtered[::-1]

if __name__ == "__main__":
    samples = [
        "racecar",
        "RaceCar"
        "A man, a plan, a canal: Panama",
        "No lemon, no melon",
        "hello",
        ""
    ]
    for t in samples:
        print(f"'{t}' -> {is_palindrome(t)}")
