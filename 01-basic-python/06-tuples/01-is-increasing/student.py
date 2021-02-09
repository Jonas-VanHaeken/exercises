# Write your code here
def is_increasing(ns):
    for n in range(0,len(ns)-1):
        if ns[n] > ns[n+1]:
            return False
    return True