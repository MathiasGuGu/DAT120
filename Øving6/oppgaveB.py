
import matplotlib.pyplot as plt


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


def plot():
    plt.plot(tid_siden_start, temp, "-", label="Temp - celsius")
    plt.plot(tid_siden_start, trykk_abs, "-", label="Trykk - abs")
    plt.legend()
    plt.show()

plot()