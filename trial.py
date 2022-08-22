from PIL import Image
import matplotlib.pyplot as plt
import csv
import os


# for i in range(100):
#     im = Image.open("./data/train/train/{}.tif".format(i))
#     im.save("./data/train/images/{}.png".format(i))


ids, labels = [], []
c = 0



with open("./data/train_labels.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        ids.append(int(row[0]))
        labels.append(int(row[1]))
        if (c:=c+1) == 20:
            break

# Sort 2 lists preserving the relationship
indexes = list(range(len(labels)))
indexes.sort(key=labels.__getitem__)
ids = list(map(ids.__getitem__, indexes))
labels = list(map(labels.__getitem__, indexes))


plt.bar(ids, labels)
plt.rcParams["figure.autolayout"] = True
plt.savefig("./train_labels.png", dpi=600)
