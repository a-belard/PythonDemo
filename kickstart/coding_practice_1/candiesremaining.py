def candies_remaining(children, candies):
    return sum(candies) % children


for i in range(int(input())):
    bags, n_children = input().split(" ")
    candies_array = [int(k) for k in input().split(" ")]
    print("Case #{}: {}".format(i + 1, candies_remaining(int(n_children), candies_array)))

