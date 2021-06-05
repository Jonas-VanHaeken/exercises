# Write your solution in this file
import imghdr

with open("output.txt",'w') as output:
    for i in range(1,101):
        filetype = imghdr.what(str(i)+".unknown")
        output.write("mv " +  str(i)+".unknown " + str(i) + "." + filetype + "\n" )
