# TASK 8.3: Sentence Palindrome Check
import unicodedata


def is_sentence_palindrome(sentence):
    """
    Return True if the sentence is a palindrome after removing spaces
    and punctuation and ignoring case; otherwise return False.
    Only alphanumeric characters are considered.
    """
    if not isinstance(sentence, str):
        return False

    # Normalize Unicode and keep only alphanumeric, compare case-insensitively
    normalized = unicodedata.normalize("NFKC", sentence)
    filtered_chars = [ch.lower() for ch in normalized if ch.isalnum()]
    if not filtered_chars:
        # Define empty-after-cleaning as True (symmetrical), can be adjusted if required
        return True
    return filtered_chars == list(reversed(filtered_chars))


def _run_tests():
    # True cases (classic palindromes ignoring case/spaces/punctuation)
    true_cases = [
        "A man, a plan, a canal: Panama!",
        "No lemon, no melon",
        "Was it a car or a cat I saw?",
        "Madam I'm Adam",
        "Never odd or even",
        "Able was I ere I saw Elba",
        "Rats live on no evil star",
        "Step on no pets",
        "Eva, can I see bees in a cave?",
        "12321",
        "1a2B2a1",
        "",  # empty -> True by definition here
        "!!!   ",  # only punctuation/spaces -> True after cleaning
    ]

    # False cases
    false_cases = [
        "This is not a palindrome",
        "Hello, World!",
        "Palindrome",           # single word not symmetrical
        "12345",
        "abcde",
        "A man, a plan, a canal: Panama? no",  # trailing non-palindromic part
        None,                    # non-string -> False
        12345,                   # non-string -> False
    ]

    print("Running sentence palindrome tests (printing True/False for each case)...")

    for s in true_cases:
        got = is_sentence_palindrome(s)
        print(f"{got} -> {s!r}")
        assert got is True, f"Expected True for: {s!r}"

    for s in false_cases:
        got = is_sentence_palindrome(s)
        print(f"{got} -> {s!r}")
        assert got is False, f"Expected False for: {s!r} (got {got})"


if __name__ == "__main__":
    _run_tests()
    print("Sentence palindrome function passing test suite")
