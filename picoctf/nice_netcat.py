myfile = open("nice_netcat.txt", "r")
mystr = ""
for i in myfile:
    mystr += chr(int(i))

print(mystr)