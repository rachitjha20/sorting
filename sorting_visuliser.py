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


def insertion_sort():
    for i in range(1,  n):
        value = lst[i]
        j = i
        
        while j > 0 and lst[j-1] > value:
            lst[j] = lst[j-1]
            j = j - 1
            plt.xlabel(f"{lst}")
        lst[j] = value
        plt.title("Insertion Sort")
        plt.bar(x, lst, color='blue')
        plt.pause(0.05)
        plt.clf()

    plt.title("Insertion Sort")
    plt.xlabel(f"{lst}")    
    plt.bar(x, lst, color='green')  # Final sorted list in green
    plt.show()   


def merge_sort(lst, x):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half, x[:mid])
        merge_sort(right_half, x[mid:])

        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

        # Update x to match the current length of lst
        plt.title("Merge Sort")
        plt.bar(x[:len(lst)], lst, color='blue')
        plt.pause(0.1)
        plt.clf()

    if len(lst) == len(x):  # This checks if we're back at the top level
        plt.title("Merge Sort")
        plt.bar(x, lst, color='green')
        plt.show()


def quick_sort():
    pass










    
a = int(input("What sorting would you opt for \n 1. Bubble Sort \n 2. Selection Sort \n 3. Insertion Sort \n 4. Merge Sort: \n"))

if a == 1:
    bubble_sort()
elif a == 2:
    selection_sort()
elif a == 3:
    insertion_sort()
elif a == 4:
    merge_sort(lst, x)
else:
    print('Enter correct option in numeric form.')