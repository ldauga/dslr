import os
import sys

from matplotlib.widgets import Button
from Utils.file_utils import open_file, parse_file, transform_file_data
from Utils.my_math import my_len, my_max, my_min
import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self, file_data, keys):
        self.file_data = file_data
        self.keys = keys
        self.index = 0
        self.fig, self.ax = plt.subplots()
        self.scatter = None
        self.update_plot()
        self.create_buttons()
        
    def update_plot(self):
        key_selected = self.keys[self.index]
        x_data = [i for i in range(my_len(self.file_data))]
        y_data = [item[key_selected] for item in self.file_data]
        
        if self.scatter:
            self.scatter.remove()
        self.scatter = self.ax.scatter(x_data, y_data, label=key_selected)
        self.ax.set_ylim(my_min(y_data) - abs(my_max(y_data) *.1), my_max(y_data) + abs(my_max(y_data) *.1))
        self.ax.legend()
        self.ax.set_title(f'Scatter plot for {key_selected}')
        self.fig.canvas.draw_idle()
    
    def next_key(self, event):
        self.index = (self.index + 1) % len(self.keys)
        self.update_plot()
    
    def prev_key(self, event):
        self.index = (self.index - 1) % len(self.keys)
        self.update_plot()
    
    def create_buttons(self):
        axprev = plt.axes([0.7, 0.01, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.01, 0.1, 0.075])
        
        self.bnext = Button(axnext, 'Next')
        self.bnext.on_clicked(self.next_key)
        
        self.bprev = Button(axprev, 'Prev')
        self.bprev.on_clicked(self.prev_key)

if my_len(sys.argv) < 2:
    print("Need arg.")
else:
    if not os.path.isfile(sys.argv[1]):
        print("File not found.")
    else:
        DATASET_PATH = sys.argv[1]
        
        with open_file(sys.argv[1]) as file:
            file_data = parse_file(file)

            file_data = transform_file_data(file_data)

            keys_possible = [key for key in file_data[0] if isinstance(file_data[0][key], float) and key != 'Index']
            current_key_index = 0

            scatter_plot = ScatterPlot(file_data, keys_possible)
            plt.show()
            