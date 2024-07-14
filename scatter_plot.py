import os
import sys

from matplotlib.widgets import Button
from Utils.file_utils import (
    open_file,
    parse_file,
    parse_file_data_by_house,
    transform_file_data,
)
from Utils.my_math import my_len, my_max, my_min
import matplotlib.pyplot as plt


class ScatterPlotCourses:
    def __init__(self, houses_data, keys):
        self.houses_data = houses_data
        self.keys = keys
        self.index = 0
        self.fig, self.ax = plt.subplots()
        self.scatterSlytherin = None
        self.scatterRavenclaw = None
        self.scatterGryffindor = None
        self.scatterHufflepuff = None
        self.update_plot()
        self.create_buttons()

    def update_plot(self):
        key_selected = self.keys[self.index]

        if self.scatterSlytherin:
            self.scatterSlytherin.remove()
        if self.scatterRavenclaw:
            self.scatterRavenclaw.remove()
        if self.scatterGryffindor:
            self.scatterGryffindor.remove()
        if self.scatterHufflepuff:
            self.scatterHufflepuff.remove()

        min_value = None
        max_value = None

        for house, data, color in [
            ("Slytherin", self.houses_data["Slytherin"], "green"),
            ("Ravenclaw", self.houses_data["Ravenclaw"], "blue"),
            ("Gryffindor", self.houses_data["Gryffindor"], "red"),
            ("Hufflepuff", self.houses_data["Hufflepuff"], "yellow"),
        ]:
            x_data = [i for i in range(my_len(data))]
            y_data = [item[key_selected] for item in data]

            if min_value == None or my_min(y_data) < min_value:
                min_value = my_min(y_data)
            if max_value == None or my_max(y_data) > max_value:
                max_value = my_max(y_data)

            if house == "Slytherin":
                self.scatterSlytherin = self.ax.scatter(
                    x_data, y_data, label=house, color=color
                )
            if house == "Ravenclaw":
                self.scatterRavenclaw = self.ax.scatter(
                    x_data, y_data, label=house, color=color
                )
            if house == "Gryffindor":
                self.scatterGryffindor = self.ax.scatter(
                    x_data, y_data, label=house, color=color
                )
            if house == "Hufflepuff":
                self.scatterHufflepuff = self.ax.scatter(
                    x_data, y_data, label=house, color=color
                )
            self.ax.legend()
            self.ax.set_title(f"Scatter plot for {key_selected} of each houses")
        self.ax.set_ylim(
            min_value - abs(max_value) * 0.1,
            max_value + abs(max_value) * 0.1,
        )
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

        self.bnext = Button(axnext, "Next")
        self.bnext.on_clicked(self.next_key)

        self.bprev = Button(axprev, "Prev")
        self.bprev.on_clicked(self.prev_key)


class ScatterPlotHouses:
    def __init__(self, houses_data):
        self.houses_data = houses_data
        self.display_arithmancy = False
        self.index = 0
        self.fig, self.ax = plt.subplots()
        self.scatter = None
        self.update_plot()
        self.create_buttons()

    def update_plot(self):
        house_selected = [
            "Slytherin",
            "Ravenclaw",
            "Gryffindor",
            "Hufflepuff",
        ][self.index]

        if self.scatter:
            self.scatter.remove()

        min_value = None
        max_value = None

        data = self.houses_data[house_selected]
        
        x_data = [i for i in range(my_len(data) * (my_len(data[0]) - (1 if not self.display_arithmancy else 0)))]
        y_data = []
        for item in data:
            for key in item:
                if key == 'Arithmancy' and not self.display_arithmancy:
                    pass
                else:
                    y_data.append(item[key])

        if min_value == None or my_min(y_data) < min_value:
            min_value = my_min(y_data)
        if max_value == None or my_max(y_data) > max_value:
            max_value = my_max(y_data)

        if house_selected == "Slytherin":
            self.scatter = self.ax.scatter(
                x_data, y_data, label=house_selected, color="green"
            )
        if house_selected == "Ravenclaw":
            self.scatter = self.ax.scatter(
                x_data, y_data, label=house_selected, color="blue"
            )
        if house_selected == "Gryffindor":
            self.scatter = self.ax.scatter(
                x_data, y_data, label=house_selected, color="red"
            )
        if house_selected == "Hufflepuff":
            self.scatter = self.ax.scatter(
                x_data, y_data, label=house_selected, color="yellow"
            )
            self.ax.legend()
            self.ax.set_title(f"Scatter plot for {house_selected} of each houses")
        self.ax.set_ylim(
            min_value - abs(max_value) * 0.1,
            max_value + abs(max_value) * 0.1,
        )
        self.fig.canvas.draw_idle()

    def next_key(self, event):
        self.index = (self.index + 1) % 4
        self.update_plot()

    def prev_key(self, event):
        self.index = (self.index - 1) % 4
        self.update_plot()
        
    def toggle_display_arithmancy(self, event):
        self.display_arithmancy = not self.display_arithmancy
        self.update_plot()

    def create_buttons(self):
        axprev = plt.axes([0.7, 0.01, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.01, 0.1, 0.075])
        
        axtoggle = plt.axes([0.1, 0.01, 0.3, 0.075])
        
        self.btoggle = Button(axtoggle, "Toggle Display Arithmancy")
        self.btoggle.on_clicked(self.toggle_display_arithmancy)

        self.bnext = Button(axnext, "Next")
        self.bnext.on_clicked(self.next_key)

        self.bprev = Button(axprev, "Prev")
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

            houses_data = parse_file_data_by_house(file_data)

            file_data = transform_file_data(file_data)

            keys_possible = [
                key
                for key in file_data[0]
                if isinstance(file_data[0][key], float) and key != "Index"
            ]
            current_key_index = 0

            scatter_plot = ScatterPlotCourses(houses_data, keys_possible)
            scatter_plot_house = ScatterPlotHouses(houses_data)

            plt.show()
