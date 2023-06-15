import json
import pickle

test_str = '{"width":500,"height":500,"resolution":96,"quality":96,"settings":[{"filename":"_preview1.jpg","seek":10},{"filename":"_preview2.jpg","seek":35},{"filename":"_preview3.jpg","seek":70},{"filename":"_preview4.jpg","seek":95}]}'

res = json.loads(test_str)
print(res)
print(type(res))

print(type(res["settings"]))
print(type(res["settings"][0]))

res["settings"] = tuple(res["settings"])
print(res)

with open("test_settings.json", 'w') as f:
    json.dump(res, f)

with open("test_settings.json", 'r') as f:
    res = json.load(f)

print(res)


res["settings"] = tuple(res["settings"])
print(res)

with open("test_settings.pickle", 'wb') as f:
    pickle.dump(res, f)

with open("test_settings.pickle", 'rb') as f:
    res = pickle.load(f)

print(res["settings"])

serilize_s = pickle.dumps(print)
new_print = pickle.loads(serilize_s)

print(new_print)

new_print("this", "is", "new", "print")