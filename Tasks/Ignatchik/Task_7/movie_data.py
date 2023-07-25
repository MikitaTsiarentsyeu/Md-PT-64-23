import json

line = ""

with open(f"short_top250.json", "r", encoding="utf-8") as f:
    line = f.read()
    
data=json.loads(line)
# print(data[12])
# print(data)