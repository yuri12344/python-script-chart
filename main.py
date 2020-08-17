import matplotlib.pyplot as plt
import numpy as np
from random import randrange

LINECOLOR = '#2ca02c' # custome line color by changing this with valid hex color
SHADECOLOR = '#8c564b' # 

im = plt.imread('./logo.png')

fig, ax = plt.subplots()

# replace with your data
xData = range(10)
yData = [randrange(-5, 10) for i in range(10)]

# get min, max, step for gradient shade
yMin = min(yData)
yMax = max(yData)
yStep = (yMax - yMin) / 100

# draw line chart
ax.plot(xData, yData, color=LINECOLOR)

# setting for bg and axis
ax.set_facecolor('k')
# ax.xaxis.label.set_color('w')
# ax.tick_params(axis='y', colors='w')
ax.axis('off') # turn off axis

# draw gradient shade
for x in range (0,100):
    Max = np.asarray([yMin + yStep * x] * 10)
    plt.fill_between(xData, yMin + yStep * x , yData, where=yData >Max,interpolate=True,  facecolor=SHADECOLOR, alpha=0.01)

# add logo, customize position and size
newax = fig.add_axes([0.15, 0.7, 0.1, 0.1], anchor='NE', zorder=1)
newax.imshow(im)
newax.axis('off')

# save image
plt.savefig('./out.png', facecolor='k', bbox_inches='tight')