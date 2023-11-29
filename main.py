import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")

yr = pd.read_csv(r"./data/yr.csv")
storm = pd.read_csv(r"./data/storm.csv")

yrData = yr["Yr Temperatur (°C)"].to_numpy()
stormData = storm["Storm Temperatur (°C)"].to_numpy()

# Igjen, inspirasjon fra Ola
average = []

for i in range(yrData.size):
    average.append(np.average([yrData[i], stormData[i]]))

yrAverage = np.average(yrData)
stormAverage = np.average(stormData)

totalAverage = np.average([yrAverage, stormAverage])

plot = yr.plot(x="Dato", y="Yr Temperatur (°C)", color="#0000ff")
storm.plot(x="Dato", y="Storm Temperatur (°C)", ax=plot, color='#ff0000')
# Credit til Ola for ideen
try:
    plt.get_current_fig_manager().full_screen_toggle()
except:
    print("Failed to get current fig manager.")

plt.plot(average, color="#2f2f2f", linestyle='--')

plot.set_xlim(left=0, right=8)

plt.yticks([-8, -6, -4, -2, 0, 2, 4, 6, 8])
plt.axhline(y=0, color='#2f2f2f', linestyle='--')
plt.axhline(yrAverage, color='#000088', linestyle='--', label="Yr Gjennomsnitt")
plt.axhline(stormAverage, color='#880000', linestyle='--', label="Storm Gjennomsnitt")
# plt.axhline(totalAverage, color='purple', linestyle='--', label="Totalt Gjennomsnitt")
plt.title("Temperatur i Kristiansund de neste 9 dagene.", fontdict={"size":"20"})

plt.xlabel("")
plt.legend()
plt.show()