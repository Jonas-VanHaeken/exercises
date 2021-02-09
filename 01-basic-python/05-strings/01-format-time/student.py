# Write your code here
def format_time(h,m,s):
    return str(h).rjust(2,'0') + ':' + str(m).rjust(2,'0')  + ':' + str(s).rjust(2,'0') 