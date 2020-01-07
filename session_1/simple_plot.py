from matplotlib import pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.plot([1, 2, 3], [10, 20, 30])
plt.title('this is the plot title')
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')
plt.legend(['Data set 1', 'Data set 2'])
plt.show()
