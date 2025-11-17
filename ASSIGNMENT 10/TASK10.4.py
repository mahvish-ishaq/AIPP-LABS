#TASK 4 – Modularize Long Function
def calculate_average(scores):
    """Return the average of all scores."""
    return sum(scores) / len(scores)


def find_highest(scores):
    """Return the highest score from the list."""
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest


def find_lowest(scores):
    """Return the lowest score from the list."""
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    """Process scores and print average, highest, and lowest."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
scores = list(map(int, input("Enter scores separated by space: ").split()))
process_scores(scores)
