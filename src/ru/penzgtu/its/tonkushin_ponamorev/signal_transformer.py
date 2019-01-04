import serial
from matplotlib import pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=5)
ser.flush()

x_len = 200
y_range = [-3, 3]

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
ys1 = [0] * x_len
ys2 = [0] * x_len
ys3 = [0] * x_len
axes1.set_ylim(y_range)
axes2.set_ylim(y_range)
axes3.set_ylim(y_range)

line1, = axes1.plot(xs, ys1)
line2, = axes2.plot(xs, ys2)
line3, = axes3.plot(xs, ys3)


def animate(ysx, ysy, ysz):
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
            ysx.append(x_value)
            ysy.append(y_value)
            ysz.append(z_value)

    except ValueError:
        print("Incorrect value!")

    ysx = ysx[-x_len:]
    ysy = ysy[-x_len:]
    ysz = ysz[-x_len:]

    line1.set_ydata(ysx)
    line2.set_ydata(ysy)
    line3.set_ydata(ysz)

    return line1, line2, line3


ani = animation.FuncAnimation(figure, animate, fargs=(ys1, ys2, ys3), interval=10, blit=True)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()

ser.close()
