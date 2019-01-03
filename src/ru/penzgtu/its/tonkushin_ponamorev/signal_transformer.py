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


def animate(ys1, ys2, ys3):
    try:
        Xvalue = float(ser.readline().rstrip())
        Yvalue = float(ser.readline().rstrip())
        Zvalue = float(ser.readline().rstrip())
        endValue = ser.readline()
        ys1.append(Xvalue)
        ys2.append(Yvalue)
        ys3.append(Zvalue)

    except ValueError:
        print("Incorrect value!")

    ys1 = ys1[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]

    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)

    return line1, line2, line3
