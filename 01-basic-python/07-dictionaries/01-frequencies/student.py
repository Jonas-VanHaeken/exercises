# Write your code here
def frequencies(xs):
    result = {}
    for item in xs:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result