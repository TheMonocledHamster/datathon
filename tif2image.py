from PIL import Image
import csv


ids, labels = [], []
c = 0
RANGE = 160

with open("./data/train_labels.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        ids.append(int(row[0]))
        labels.append(int(row[1]))
        if (c:=c+1) == RANGE:
            break


for i in range(RANGE):
    im = Image.open("./data/train/train/{}.tif".format(i))
    im.save("./data/train/images/{}.png".format(str(labels[i])+'_'+str(i)))
