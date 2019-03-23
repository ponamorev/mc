import serial
from matplotlib import pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
ser.flush()

x_len = 200
y_range = [-5, 5]

figure = plt.figure()

axes1 = figure.add_subplot(1, 3, 1)
plt.title("X")
plt.xlabel("Time")
plt.ylabel("Acceleration")

axes2 = figure.add_subplot(1, 3, 2)
plt.title("Y")
plt.xlabel("Time")
plt.ylabel("Acceleration")

axes3 = figure.add_subplot(1, 3, 3)
plt.title("Z")
plt.xlabel("Time")
plt.ylabel("Acceleration")

plt.suptitle("Output from accelerometer")

xs = list(range(0, 200))
outFromAcc_1 = [0] * x_len
outFromAcc_2 = [0] * x_len
outFromAcc_3 = [0] * x_len
axes1.set_ylim(y_range)
axes2.set_ylim(y_range)
axes3.set_ylim(y_range)

line1, = axes1.plot(xs, outFromAcc_1)
line2, = axes2.plot(xs, outFromAcc_2)
line3, = axes3.plot(xs, outFromAcc_3)


def animate(dir_x, dir_y, dir_z):
    try:
        line_from_accelerator = ser.readline().rstrip()
        if line_from_accelerator[0] != '$':
            print("Bad string " + line_from_accelerator)
            print("Incoming string should start with \'$\'")
        else:
            list_of_values = line_from_accelerator[1:].split("|")
            x_value = float(list_of_values[0])
            y_value = float(list_of_values[1])
            z_value = float(list_of_values[2])
            dir_x.append(x_value)
            dir_y.append(y_value)
            dir_z.append(z_value)

    except ValueError:
        print("Incorrect value!")

    dir_x = dir_x[-x_len:]
    dir_y = dir_y[-x_len:]
    dir_z = dir_z[-x_len:]

    line1.set_ydata(dir_x)
    line2.set_ydata(dir_y)
    line3.set_ydata(dir_z)

    return line1, line2, line3


ani = animation.FuncAnimation(figure, animate, fargs=(outFromAcc_1, outFromAcc_2, outFromAcc_3), interval=10, blit=True)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()

ser.close()
