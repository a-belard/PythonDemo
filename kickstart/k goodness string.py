def goodness_string(s, k):
    k_goodness = 0
    for i in range(int(len(s) / 2)):
        if s[i] != s[-i-1]:
            k_goodness += 1

    if k_goodness < k:
        return k - k_goodness
    else:
        return 0


for i in range(int(input())):
    n, k = input().split(" ")
    s = input("")
    print("Case #{}: {}".format(1, goodness_string(s.upper(), int(k))))
