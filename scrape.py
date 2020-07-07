import json
import os
import time

os.system("scrape.bat")
with open("sole_nyu/sole_nyu.json", "r", encoding = "utf-8") as file:
    read = json.load(file)
data = read["GraphImages"][0]["comments"]["data"]
array = []
total = 0
yes = 0
no = 0
for comment in data:
    total += 1
    if "C" in comment["text"]:
        yes += 1
    else:
        no += 1
total_percentage = str((yes / (yes + no)) * 100)[:5]
print(f"{total_percentage}% of people voted C.")
