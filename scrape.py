import json
import os
import time

os.system("scrape.bat")
with open("sole_nyu/sole_nyu.json", "r", encoding = "utf-8") as file:
    read = json.load(file)
data = read["GraphImages"][0]["comments"]["data"]
array = []
for comment in data:
    array.append(comment["text"])
