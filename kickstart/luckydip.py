def luckydip(values_size, redips, values):
    values = sorted(values)
    value = sum(values) / values_size
    formervalue = value
    while redips > 0:
        less_than_formervalue = 0
        for i in values:
            if i > formervalue:
                break
            less_than_formervalue += 1
        value = ((less_than_formervalue * formervalue) + sum(values[less_than_formervalue:])) / values_size
        formervalue = value
        redips -= 1
    return value


for i in range(int(input())):
    values_size, redips = [int(k) for k in input().split(" ")]
    print("Case #{}= {}".format(i, luckydip(values_size, redips, [int(j) for j in input().split(" ")][0:values_size])))