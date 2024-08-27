import matplotlib.pyplot as plt 
import numpy as np

amount = 15

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(lst)

def bubble_sort():
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            plt.bar(x, lst, color='blue')
            plt.pause(0.05)
            plt.clf()

    plt.bar(x, lst, color='green')  # Final sorted list in green
    plt.show()


bubble_sort()