import csv

head = ["make", "model", "sku"]

with open("test.csv", 'r', newline='') as f:
    reader = csv.DictReader(f, head)
    for row in reader:
        print(row)

# with open("test.csv", 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["asics", "mexico 66", "3546543"])

# with open("test.csv", 'r', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# products = []
# head = ["make", "model", "sku"]

# isFirst = True

# with open("test.csv", 'r') as f:
#     for line in f:
#         if isFirst:
#             isFirst = False
#             continue
#         parts = line.replace("\n", '').split(',')
#         d = {}
#         for i in range(len(head)):
#             d[head[i]] = parts[i]
#         products.append(d)

# with open("test_headless.csv", 'w') as f:
#     for p in products:
#         line = ",".join(p.values()) + "\n"
#         f.write(line)
