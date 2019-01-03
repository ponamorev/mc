from matplotlib import pyplot as plt

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


manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
