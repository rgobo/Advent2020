# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import re

with open("4.txt", "r") as f:
    lines = f.read().splitlines() 
lines.append('')
lines[0:12]


# %%
class Password:
    def __init__(self, lines):
        self.dict = {}
        self.keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"] # "cid" optional
        for line in lines:
            split = line.split(' ')
            for sp in split:
                kv = sp.split(':')
                key = kv[0]
                val = kv[1]
                self.dict[key] = val

    def isInRange(self, val, min, max):
        if not val.isnumeric():
            return False
        if int(val) < min or int(val) > max:
            return False
        return True

    def isValid(self):
        for key in self.keys:
            if key not in self.dict:
                return False
        
        if not self.isInRange(self.dict["byr"], 1920, 2002):
            return False
        if not self.isInRange(self.dict["iyr"], 2010, 2020):
            return False
        if not self.isInRange(self.dict["eyr"], 2020, 2030):
            return False
        
        hgt = self.dict["hgt"]
        if hgt[-2:] == "cm":
            if not self.isInRange(hgt[:-2], 150, 193):
                return False
        elif hgt[-2:] == "in":
            if not self.isInRange(hgt[:-2], 59, 76):
                return False
        else:
            return False

        hcl = self.dict["hcl"]
        x = re.search("#[0-9a-f]{6}", hcl)
        if not x:
            return False

        ecl = self.dict["ecl"]
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        
        pid = self.dict["pid"]
        x = re.search("#[0-9]{9}", pid)
        if not x:
            return False

        return True


# %%
current = []
nOfValid = 0
for line in lines:
    if len(line) == 0:
        p = Password(current)
        current = []
        if p.isValid():
            nOfValid += 1
        continue
    current.append(line)
print(f"Result:{nOfValid}")


# %%
t = Password(lines[0:2])
t.isValid()


# %%
"test01"[:-2]


# %%
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
print ("Yes" if x else "No")


# %%
txt = "#623a2f"
x = re.search("#[0-9a-f]{6}", txt)
print ("No" if not x else "Yes")


