def centauri_prime(kingdom):
    vowels = "aeiouAeiou"
    lastletter = kingdom[-1]
    if lastletter == ".":
        lastletter = kingdom[-2]
    if lastletter == "y":
        return "{} is ruled by nobody.".format(kingdom)
    for i in vowels:
        if i == lastletter:
            return "{} is ruled by Alice.".format(kingdom)
    return "{} is ruled by Bob.".format(kingdom)


for i in range(int(input())):
    print("Case #{}: {}".format(i + 1, centauri_prime(input())))
