import json
import os
import time

os.system("scrape.bat")
with open("TARGET_USER/TARGET_USER.json", "r", encoding = "utf-8") as file:
    read = json.load(file)
data = read["GraphImages"][0]["comments"]["data"]
array = []
for comment in data:
    array.append(comment["text"])
