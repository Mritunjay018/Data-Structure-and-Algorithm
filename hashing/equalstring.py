def can_make_equal(strings):
    from collections import Counter

    n = len(strings)
    total_count = Counter()

    # Count all characters from all strings
    for s in strings:
        total_count += Counter(s)

    # Check if each character's total freq is divisible by number of strings
    for freq in total_count.values():
        if freq % n != 0:
            return "No"

    return "Yes"


# Example
strings = ["collegeee","coll","collegge"]

print(can_make_equal(strings))   # Yes
