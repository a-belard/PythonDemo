import re


def findminpresses(num):
    initialnum = num
    num = int(num)
    num2 = int(num)
    odd = "[13579]"
    while re.search(odd, str(num)) and re.search(odd, str(num2)):
        num += 1
        num2 -= 1
    return min(num - initialnum, initialnum - num2)


for i in range(int(input())):
    print(f"#{i+1}: {findminpresses(int(input()))}")
