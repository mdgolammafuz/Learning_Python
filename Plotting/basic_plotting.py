import matplotlib.pyplot as plt
import numpy as np  # importing numpy
x = np.arange(11)  # using arange to create array "x"
y = x ** 2  # computing square of "x"
print("original array is:", x)  # a normal print statement
print("Square of original array is:", y)  # a normal print statement
plt.plot(x, y)
# We can add labels and title
plt.xlabel('X Axis Title')
plt.ylabel('Y Axis Title')
plt.title('Figure/plot Title')
plt.show()

# plt.subplot(nrows, ncols, plot_number)

# For plot on left
plt.subplot(1, 3, 1)  # (131) is same as (1,3,1)
plt.plot(x, y, 'r--')

# For plot in the middle
plt.subplot(1, 3, 2)
plt.plot(y, x, 'g*-')

# For the plot on right
plt.subplot(1, 3, 3)
plt.plot(x, y, 'r--')
plt.plot(y, x, 'g*-')

# Let's adjust the subplots
plt.tight_layout()  # try the same code without tight_layout() and see the difference!
plt.show()
