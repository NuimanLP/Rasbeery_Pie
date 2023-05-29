import Adafruit_DHT
import matplotlib.pyplot as plt
import numpy as np

# Set the sensor type and pin number
sensor = Adafruit_DHT.DHT11
pin = 4

# Initialize variables to store the data
temps = []
humids = []

# Set the number of data points to display
num_points = 20

# Set the refresh rate (in seconds)
refresh_rate = 5

# Set up the matplotlib plot
plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot(temps, 'r-')
line2, = ax.plot(humids, 'b-')
plt.ylim(0, 100)

# Set up the plot labels
plt.title('Temperature and Humidity')
plt.ylabel('Temperature (C) / Humidity (%)')

# Initialize the plot with empty data
line1.set_ydata(np.ma.array(temps, mask=True))
line2.set_ydata(np.ma.array(humids, mask=True))
fig.canvas.draw()

# Main loop to read data and update the plot
while True:
    # Try to get a reading from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Append the data to the lists
    temps.append(temperature)
    humids.append(humidity)

    # Limit the number of data points displayed
    temps = temps[-num_points:]
    humids = humids[-num_points:]

    # Update the plot data
    line1.set_ydata(temps)
    line2.set_ydata(humids)

    # Redraw the plot
    fig.canvas.draw()

    # Wait for the refresh rate
    plt.pause(refresh_rate)
import Adafruit_DHT
import matplotlib.pyplot as plt
import numpy as np

# Set the sensor type and pin number
sensor = Adafruit_DHT.DHT11
pin = 4

# Initialize variables to store the data
temps = []
humids = []

# Set the number of data points to display
num_points = 20

# Set the refresh rate (in seconds)
refresh_rate = 5

# Set up the matplotlib plot
plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot(temps, 'r-')
line2, = ax.plot(humids, 'b-')
plt.ylim(0, 100)

# Set up the plot labels
plt.title('Temperature and Humidity')
plt.ylabel('Temperature (C) / Humidity (%)')

# Initialize the plot with empty data
line1.set_ydata(np.ma.array(temps, mask=True))
line2.set_ydata(np.ma.array(humids, mask=True))
fig.canvas.draw()

# Main loop to read data and update the plot
while True:
    # Try to get a reading from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Append the data to the lists
    temps.append(temperature)
    humids.append(humidity)

    # Limit the number of data points displayed
    temps = temps[-num_points:]
    humids = humids[-num_points:]

    # Update the plot data
    line1.set_ydata(temps)
    line2.set_ydata(humids)

    # Redraw the plot
    fig.canvas.draw()

    # Wait for the refresh rate
    plt.pause(refresh_rate)
