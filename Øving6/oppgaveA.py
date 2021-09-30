import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter

import numpy as np

fil = "/Users/mathiasgumpen/Desktop/Dat120/Øving6/trykk_og_temperaturlogg.csv"

temp = []
dato = []
tid_siden_start = []
trykk = []

def read():
    with open(fil) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\tdato og tid: {row[0]}, Tid siden start (sek): {row[1]} Trykk (Bar): {row[3]}, Temperatur (Celsius): {row[4]}.')
                temp.append(row[4])
                dato.append(row[0])
                tid_siden_start.append((float(row[1]) / 60))
                trykk.append(row[2])
                line_count += 1
        print(f'Processed {line_count} lines.')

def write():
    with open("/Users/mathiasgumpen/Desktop/Dat120/Øving6/logg.txt", "w") as writer:
        for item in sorted(trykk):
            writer.write(item + "\n")



def create_plot():
        """
        plt.ylabel('Temperatur (Celsius)', fontsize=10)
        plt.xlabel('Tid etter start (Min)', fontsize=10)
        plt.grid(True)
        plt.legend(fontsize=40, loc=10) 


        plt.plot(tid_siden_start, temp, linestyle = "--", label="Temperatur")
        plt.show()

        """
        fig = plt.figure(figsize=(10, 3))
        ax = fig.add_subplot(111)
        plt.yticks(np.arange(0,len(temp),100))
        plt.xticks(np.arange(0,len(tid_siden_start),500))
        ax.plot(tid_siden_start, (temp))
        plt.show()
read()
write()
create_plot()
