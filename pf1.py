from pprint import pprint

data = [
    {"from": "B", "to": "E"},
    {"from": "A", "to": "C"},
    {"from": "F", "to": "B"},
    {"from": "C", "to": "F"},
    {"from": "D", "to": "A"},
]

_from_, _tu_ = [], []

for i in data:
    _from_.append(i["from"])
    _tu_.append(i["to"])

print(_from_)
print(_tu_)

[start] = [i for i in _from_ if i not in _tu_]
print(start)
new_data = []
cur = ""

while len(new_data) != len(data):
    for elem in data:
        pass
        if len(new_data) == 0 and elem.get("from") == start:
            new_data.append(elem)
            cur = elem["to"]
        else:
            if elem.get("from") == cur:
                new_data.append(elem)
                cur = elem["to"]

pprint(new_data, indent=4)
