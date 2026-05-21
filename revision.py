import os
import random 

problems = []

for root, dirs, files in os.walk(os.path.dirname(__file__), topdown=False):
    for folder in dirs:
        first_uni = ord(folder[0]) - ord("0")
        if len(folder) > 2 and first_uni <= 9 and first_uni >= 0:
            problems.append(folder)

print("Random Problem: " + problems[random.randint(0, len(problems) - 1)])
