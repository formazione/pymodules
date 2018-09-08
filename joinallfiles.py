import os


files = [f for f in os.listdir()]

try:
    for f in files:
        print(f"# =========={f}============")
        for line in open(f, 'r', encoding='utf-8'):
            print(line.rstrip())
        print(f"# ======== end {f} ==========\n\n")
except:
    print("Try this code with only txt files in it")
