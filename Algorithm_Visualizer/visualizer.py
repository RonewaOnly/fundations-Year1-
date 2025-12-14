from tkinter import *
import heapq
import time
from threading import Thread
from queue import PriorityQueue

class SorterMethods:
    
    def __init__(self, visualizer):
        self.visualizer = visualizer
        self.sorting = False
        self.speed = 0.1  # Default speed
        self.algorithm = None
    
    def set_algorithm(self, algorithm): # Set the sorting algorithm
        self.algorithm = algorithm
        self.visualizer.update_algorithm_label(algorithm)# Set the sorting algorithm
    
    def set_speed(self, speed): # Set the speed of visualization
        self.speed = speed
        self.visualizer.update_speed_label(speed)# Set the speed of visualization
    
    def start_sorting(self):# Start the sorting process
        if self.algorithm and not self.sorting: # Start the sorting process
            self.sorting = True
            thread = Thread(target=self.run_sorting_algorithm)#
            thread.start()
    def stop_sorting(self):
        self.sorting = False# Stop the sorting process
        
    def bubble_sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if not self.sorting:
                    return
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    self.visualizer.update_visualization(data, [j, j+1])
                    time.sleep(self.speed)
        self.visualizer.update_visualization(data)
        
    def selection_sort(self, data):
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if not self.sorting:
                    return
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            self.visualizer.update_visualization(data, [i, min_idx])
            time.sleep(self.speed)
        self.visualizer.update_visualization(data)
        
    def insertion_sort(self, data):
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i-1
            while j >=0 and key < data[j]:
                if not self.sorting:
                    return
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            self.visualizer.update_visualization(data, [j + 1, i])
            time.sleep(self.speed)
        self.visualizer.update_visualization(data)
        
    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            L = data[:mid]
            R = data[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if not self.sorting:
                    return
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1
                self.visualizer.update_visualization(data)
                time.sleep(self.speed)

            while i < len(L):
                if not self.sorting:
                    return
                data[k] = L[i]
                i += 1
                k += 1
                self.visualizer.update_visualization(data)
                time.sleep(self.speed)

            while j < len(R):
                if not self.sorting:
                    return
                data[k] = R[j]
                j += 1
                k += 1
                self.visualizer.update_visualization(data)
                time.sleep(self.speed)
    def quick_sort(self, data, low, high):
        if low < high:
            pi = self.partition(data, low, high)

            self.quick_sort(data, low, pi - 1)
            self.quick_sort(data, pi + 1, high)
    def partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if not self.sorting:
                return
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                self.visualizer.update_visualization(data, [i, j])
                time.sleep(self.speed)
        data[i + 1], data[high] = data[high], data[i + 1]
        self.visualizer.update_visualization(data, [i + 1, high])
        time.sleep(self.speed)
        return i + 1
    
    def heap_sort(self, data):
        n = len(data)
        heapq.heapify(data)
        sorted_data = []
        for _ in range(n):
            if not self.sorting:
                return
            smallest = heapq.heappop(data)
            sorted_data.append(smallest)
            self.visualizer.update_visualization(sorted_data + data)
            time.sleep(self.speed)
        data.extend(sorted_data)
        self.visualizer.update_visualization(data)
    def cycle_sort(self, data):
        n = len(data)
        for i in range(n):
            if not self.sorting:
                return
            item = data[i]
            pos = i
            for j in range(i + 1, n):
                if data[j] < item:
                    pos += 1
            if pos == i:
                continue
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
            while pos != i:
                pos = i
                for j in range(i + 1, n):
                    if data[j] < item:
                        pos += 1
                while item == data[pos]:
                    pos += 1
                data[pos], item = item, data[pos]
                self.visualizer.update_visualization(data)
                time.sleep(self.speed)
        self.visualizer.update_visualization(data)
        
    def run_sorting_algorithm(self):
        data = self.visualizer.get_data_copy()
        if self.algorithm == "Bubble Sort":
            self.bubble_sort(data)
        elif self.algorithm == "Selection Sort":
            self.selection_sort(data)
        elif self.algorithm == "Insertion Sort":
            self.insertion_sort(data)
        elif self.algorithm == "Merge Sort":
            self.merge_sort(data)
        elif self.algorithm == "Quick Sort":
            self.quick_sort(data, 0, len(data) - 1)
            self.visualizer.update_visualization(data)
        elif self.algorithm == "Heap Sort":
            self.heap_sort(data)
        elif self.algorithm == "Cycle Sort":
            self.cycle_sort(data)
        self.sorting = False
        
class Visualizer:
    def __init__(self, root):
        self.root = root
        self.data = []
        self.sorter = SorterMethods(self)
        self.algorithm_label = Label(root, text="Algorithm: None")
        self.algorithm_label.pack()
        self.speed_label = Label(root, text="Speed: 0.1s")
        self.speed_label.pack()
        self.canvas = Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()
        
    def update_algorithm_label(self, algorithm):
        self.algorithm_label.config(text=f"Algorithm: {algorithm}")
        
    def update_speed_label(self, speed):
        self.speed_label.config(text=f"Speed: {speed}s")
        
    def update_visualization(self, data, highlight_indices=[]):
        self.canvas.delete("all")
        canvas_height = 400
        canvas_width = 600
        bar_width = canvas_width / len(data)
        max_value = max(data) if data else 1
        
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = canvas_height - (value / max_value) * canvas_height
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            
            color = 'red' if i in highlight_indices else 'blue'
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        
        self.root.update_idletasks()
        
    def get_data_copy(self):
        return self.data.copy()
    
#menu options which sorting algorithm to visualize menu options
def menu_options():
    root.menu = Menu(root)
    root.config(menu=root.menu)
    algorithm_menu = Menu(root.menu, tearoff=0)
    root.menu.add_cascade(label="Algorithms", menu=algorithm_menu)
    algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Cycle Sort"]
    for algo in algorithms:
        algorithm_menu.add_command(label=algo, command=lambda a=algo: visualizer.sorter.set_algorithm(a))
    return algorithms[0]  # Default to the first algorithm

# Main execution
if __name__ == "__main__":
    root = Tk()
    root.title("Sorting Algorithm Visualizer")
    visualizer = Visualizer(root)
    default_algorithm = menu_options()
    visualizer.sorter.set_algorithm(default_algorithm)
    
    # Example data
    visualizer.data = [64, 34, 25, 12, 22, 11, 90]
    visualizer.update_visualization(visualizer.data)
    
    # Start sorting button
    start_button = Button(root, text="Start Sorting", command=visualizer.sorter.start_sorting)
    start_button.pack()
    
    # Stop sorting button
    stop_button = Button(root, text="Stop Sorting", command=visualizer.sorter.stop_sorting)
    stop_button.pack()
    
    #reset data button
    def reset_data():
        visualizer.data = [64, 34, 25, 12, 22, 11, 90]
        visualizer.update_visualization(visualizer.data)
    reset_button = Button(root, text="Reset Data", command=reset_data)
    reset_button.pack()
    
    
    
    root.mainloop()