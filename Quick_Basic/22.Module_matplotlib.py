# used to plot charts
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]

# plt.plot(x, y)
# plt.show()

# changing the x axis
legends = ["jan", "feb", "mar", "apr"]
plt.xticks(x, legends)

plt.plot(x, y)
plt.show()


'''
FOR MORE 

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
https://matplotlib.org/stable/gallery/index.html

'''
