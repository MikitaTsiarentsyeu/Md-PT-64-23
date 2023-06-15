import json
import csv

keys = ["make", "model", "volume", "power", "year", "id"]
data = [    
	("Honda", "Civic", 1.5, 174, 2021, "honda_civic_2021"),
	("Toyota", "Corolla", 2.0, 169, 2022, "toyota_corolla_2022"),
    ("Ford", "Mustang", 5.0, 460, 2021, "ford_mustang_2021"),
    ("Chevrolet", "Camaro", 6.2, 455, 2022, "chevrolet_camaro_2022"),
    ("Dodge", "Charger", 3.6, 292, 2021, "dodge_charger_2021"),
    ("Nissan", "Altima", 2.5, 188, 2022, "nissan_altima_2022"),
    ("Mazda", "CX-5", 2.5, 187, 2021, "mazda_cx5_2021"),
    ("Subaru", "Impreza", 2.0, 152, 2022, "subaru_impreza_2022"),
    ("BMW", "M3", 3.0, 473, 2021, "bmw_m3_2021"),
    ("Mercedes-Benz", "C-Class", 2.0, 255, 2022, "mercedes_cclass_2022")
]

# print(json.dumps(data))

res = []
for car_data in data:
    car_dict = {}
    for i in range(len(keys)):
        car_dict[keys[i]] = car_data[i]
    res.append(car_dict)

with open("cars.json", 'w') as f:
    json.dump(res, f)


with open("cars.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    writer.writerows(data)

