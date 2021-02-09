# Write your code here
def contains_duplicates(xs):
    containsduplicates = any(xs.count(element) > 1 for element in xs)
    return containsduplicates
