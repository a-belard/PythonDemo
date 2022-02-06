import itertools
import re


def scramblewords(words, s1, s2, n, a, b, c, d):
    x1 = ord(s1)
    x2 = ord(s2)
    chars = [0] * n
    chars[0], chars[1] = x1, x2
    i = 2
    for j in range(n-2):
        chars[i] = ((a * chars[i - 1]) + (b * chars[i - 2]) + c) % d
        i += 1
    scramledstring = [s1, s2] + [chr(97 + (k % 26)) for k in chars[2:]]
    scramledstring = "".join(scramledstring)
    words_counter = 0
    words_lengths = set(int(len(j)) for j in words)
    print(words_lengths)
    distincts = set()
    for length in words_lengths:
        for i in range(n):
            myword = scramledstring[i:i + length]
            if sorted(myword) in words:
                if myword not in distincts:
                    words_counter += words.count(sorted(myword))
                    distincts.add(myword)
    return words_counter


for i in range(int(input())):
    l: int = int(input())
    words = [sorted(k) for k in input().split(" ")]
    s1, s2, n, a, b, c, d = input().split(" ")
    print("Case #{}: {}".format(i + 1, scramblewords(words, s1, s2, int(n), int(a), int(b), int(c), int(d))))
