import csv
import matplotlib.pyplot as plt

import numpy as np

fil = "/Users/mathiasgumpen/Desktop/Dat120/Øving6/trykk_og_temperaturlogg.csv"
# Temperatur (gr Celsius);

def read():
    with open(fil) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        temp = []
        tid = []

        for row in csv_reader:
            temp.append(row["Temperatur (gr Celsius)"])
            tid.append(row["Tid siden start (sek)"])

        #print(temp[1])
        #print(tid[1])
        plt.xticks()
        plt.yticks()
        plt.plot(tid, temp)

        plt.show()



read()
