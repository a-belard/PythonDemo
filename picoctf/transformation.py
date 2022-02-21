flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
let = flag[0]
print()
mystr = ""
for i in range(0, len(flag)):
    first_int = ord(flag[i]) >> 8
    first_char = chr(first_int)
    second_int = ord(flag[i]) - (first_int << 8)
    second_char = chr(second_int)
    mystr += first_char + second_char

print(mystr)

