import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import pandas as pd

plt.style.use("dark_background")

# Loads the temperature data from the .csv files.
yrData = pd.read_csv(r"./data/yr.csv")["temp"].to_numpy()
stormData = pd.read_csv(r"./data/storm.csv")["temp"].to_numpy()

# Goes through the range of temperatures and evaluates an average of the two datasets, and then puts those values into an array.
averageData = []
for i in range(yrData.size):
    averageData.append(np.average([yrData[i], stormData[i]]))
averageData = np.asarray(averageData)

plt.plot(yrData, color="#ff0000", label="Yr")
plt.plot(stormData, color="#0000ff", label="Storm")

plt.plot(averageData, color="#4f4f4f", linestyle="--", label="Average")

plt.axhline(y=0, color='#0f0f0f', linestyle='--') # Draws a line at y0.

plt.axhline(y=np.average(yrData), color='#4f0f0f', linestyle='--', label="Yr Average")
plt.axhline(y=np.average(stormData), color='#0f0f4f', linestyle='--', label="Storm Average")
plt.axhline(y=stats.mode(yrData), color='#0f4f0f', linestyle='--', label="Yr Mode")
plt.axhline(y=stats.mode(stormData), color='#4f4f0f', linestyle='--', label="Storm Mode")

# Evenly distributes the 9 dates on the x-axis.
dates = np.array(["Wed 29. Nov", "Thu 30. Nov", "Fri 1. Dec", "Sat 2. Dec", "Sun 3. Dec", "Mon 4. Dec", "Tue 5. Dec", "Wed 6. Dec", "Thu 7. Dec"])
plt.xticks(list(range(0, 9)), dates)
plt.xlim(0, 8) # Stretches the data to fit the plot.

plt.yticks(list(range(-8, 9)))

plt.title("Temperature forecast for Kristiansund the next 9 days", fontdict={"size":"20"})
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

plt.text(0.1, 0.5, "+")
plt.text(0.11, -0.5, "_")

plt.legend() # Renders the UI elements (labels) to the plot.

plt.get_current_fig_manager().full_screen_toggle() # Inspiration: Ola | Remove if problems accur
plt.show()