# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
with open("C:/dev/AdventOfCode2020/2020/7.txt", "r") as f:
    lines = f.read().splitlines()


# %%
class Bag:
    def __init__(self, text):
        split = text.split(" contain ")
        self.name = " ".join(split[0].split(" ")[:-1])

        self.canContain = {}
        if split[1] == "no other bags.":
            return
        split = split[1].split(", ")
        for c in split:
            sc = c.split(" ")
            k = " ".join(sc[1:-1])
            v = sc[0]
            #print(f"key:{k}, val:{v}")
            self.canContain[k] = v


# %%
def canContain(allBags, bag, bagName):
    if len(bag.canContain) == 0:
        return False
    if bagName in bag.canContain:
        return True
    for k, v in bag.canContain.items():
        bag = allBags[k]
        if canContain(allBags, bag, bagName):
            return True
    return False


# %%
allBags = {}
for line in lines:
    b = Bag(line)
    allBags[b.name] = b
    print(f"Key:{b.name}, canContain: {b.canContain}")


# %%
myBag = "shiny gold"

c = 0
for name, bag in allBags.items():
    if canContain(allBags, bag, myBag):
        c += 1
print(f"res:{c}")


# %%
len(allBags)
