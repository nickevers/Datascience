import numpy as np
import csv
import matplotlib.pyplot as plt


alcohol = []
quality = []

with open('../files/wine.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            alcohol.append(float(row[10]))
            quality.append((int(row[11])))
            line_count += 1

print(f"Average is {np.average(alcohol)}%")
print(f"Median is {np.median(alcohol)}%")
print(f"Max is {np.max(alcohol)}%")
print(f"Correlation is {np.corrcoef(alcohol, quality)[0]}")

plt.hist(alcohol, bins='auto')  # arguments are passed to np.histogram
plt.title("Alcohol %")
plt.show()

