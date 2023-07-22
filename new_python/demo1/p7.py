import json

list2 = ['{"k": 2}', {"e": 2}, '{"w": "k"}', ('y', 2), ('v', 5)]

for s in list2:

    if isinstance(s, str):
        w = json.loads(s)
    elif isinstance(s, tuple):

        w = dict([s])

    else:
        w = s

    print(type(w), w)
