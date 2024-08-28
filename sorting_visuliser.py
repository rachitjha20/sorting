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
                plt.xlabel(f"{lst}")
            plt.title("Bubble Sort")
            plt.bar(x, lst, color='blue')
            plt.pause(0.05)
            plt.clf()
    plt.title("Bubble Sort")
    plt.xlabel(f"{lst}")
    plt.bar(x, lst, color='green')  # Final sorted list in green
    plt.show()




def selection_sort():
    
    for i in range(n):
        min_value = lst[i]
        min_index = i
        for j in range(i+1, n):
            if lst[j] < min_value:
                min_value = lst[j]
                min_index = j
                plt.xlabel(f"{lst}")
        lst[i], lst[min_index] = lst[min_index], lst[i]
        plt.title("Selection Sort")
        plt.bar(x, lst, color='blue')
        plt.pause(0.05)
        plt.clf()
    plt.title("Selection Sort")
    plt.xlabel(f"{lst}")    
    plt.bar(x, lst, color='green')  # Final sorted list in green
    plt.show()
    
a = int(input("What sorting would you opt for \n 1. Bubble Sort \n 2. Selection Sort : \n"))

if a == 1:
    bubble_sort()
elif a == 2:
    selection_sort()
else:
    print('Enter correct option in numeric form.')