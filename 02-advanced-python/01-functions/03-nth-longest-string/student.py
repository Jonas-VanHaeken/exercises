# Write your code here
def nth_longest_string(n, strings):
    sorted_list = sorted(strings, key=len)
    return sorted_list[-n]