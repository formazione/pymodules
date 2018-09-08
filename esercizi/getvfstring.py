import os

file = [x for x in os.listdir() if x.startswith("vf_data")]


def getvfstring():
    with open(file[0], encoding='utf-8') as f:
        f = f.read()
    return f
