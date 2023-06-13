chunk_size = 1000

with open("psina.jpg", "rb") as donor:
    with open("psina_copy.jpg", "wb") as recep:
        while True:
            chunk = donor.read(chunk_size)
            if chunk:
                recep.write(chunk)
            else:
                break
print("done")