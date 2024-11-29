results = [
    {"choices":["A","B","C"], "nb":1},
    {"choices":["B","C","A"], "nb":1},
    {"choices":["C","A","B"], "nb":1}
]

pairs = {}

winners = {"value":None, "winners":[]}


def add_pair(val):
    if val in pairs :
        pairs[val] += 1
    elif val[::-1] in pairs:
        pairs[val[::-1]] -= 1
    else :
        pairs[val] = 1


for ele in results :
    for repetition in range(ele["nb"]) :
        for pair_start, pair_end in zip(ele["choices"], ele["choices"][1::1]):
            add_pair(pair_start+pair_end)


for key, value in pairs.items() :

    if winners["value"] == None :
        winners["value"] = value
        winners["winners"] = [key]

    elif value > winners["value"] :
        winners["value"] = value
        winners["winners"] = [key]

    elif value == winners["value"] :
        winners["winners"].append(key)

print(pairs)
print(winners)