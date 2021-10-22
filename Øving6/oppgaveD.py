import csv
from matplotlib import lines
import matplotlib.pyplot as plt


import numpy as np

fil = "/Users/mathiasgumpen/Desktop/Dat120/Øving6/trykk_og_temperaturlogg.csv"

temp = []
tid_siden_start = []
trykk_abs = []



def get_data():


    csv_reader = open(fil, "r")
    lines = csv_reader.readline()

    for lines in csv_reader:
        x = lines.strip()
        x2 = x.split(";")
        temp.append(float(x2[4].replace(",", ".")))
        tid_siden_start.append(float(x2[1]))
        trykk_abs.append(float(x2[3].replace(",", ".")))


    
get_data()


def finn_feil():
    imposter = []

    for i in range(len(tid_siden_start)):
        if not i == 0:
            prev = tid_siden_start[i - 1]
            if not tid_siden_start[i] - prev == 10:
                imposter.append([prev, tid_siden_start[i]])

    print(f"\n {imposter} \n")

finn_feil()