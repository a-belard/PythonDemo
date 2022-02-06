price = 0
skiers = 0

def  nextSlope(slopes, slope, expense):
    global price
    subslopes = [k for k in filter(lambda a: a["start"] == slope["end"], slopes)]
    if len(subslopes) == 0:
        mysubplots = [k for k in filter(lambda a:a["start"]==slope["start"], slopes)]

    else:
        for k in subslopes:
            nextsubslopes = nextSlope(slopes, k)
            slopeSkiers = 0

        # for i in subslopes:
        #     price += slope["price"] * slopeSkiers
        #     nextSlope(slopes, i)

def packtheslopes(slopes):
    slopes.sort(key=lambda k: k["start"])
    for i in slopes:
        if i["start"] == 1:
            nextSlope(slopes, i, i["price"]*i["skiers"])


slopes = ["4 7 2 2", "1 3 5 5", "1 4 2 -1", "3 2 3 -2", "3 5 2 -1", "3 6 2 2"]
slopes = [
    k.split(" ") for k in slopes
]

slopes = [{"start": int(j[0]), "end": int(j[1]), "skiers": int(j[2]), "price": int(j[3])} for j in slopes]

print(packtheslopes(slopes))