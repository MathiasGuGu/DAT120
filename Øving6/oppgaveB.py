
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
    fig, ax = plt.subplots(2)
    ax[0].plot(tid_siden_start, temp, "-", color="red")
    ax[0].set_title("Temp - C")
    ax[1].plot(tid_siden_start, trykk_abs, "-")
    ax[1].set_title("Trykk - BAR")
    plt.legend()
    plt.show()

plot()