# Write your solution in this file
with open("output.txt",'w') as output:
    for i in range(0,10001):
        dec = i
        binair = bin(i)
        hexa = hex(i)
        output.write(str(dec).rjust(10) +str(binair).rjust(20) + str(hexa).rjust(10) + "\n")