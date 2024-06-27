from contextlib import contextmanager

from Utils.my_math import my_len


@contextmanager
def open_file(path):
    file = open(path, 'r')
    try:
        yield file
    finally:
        file.close()

def parse_file(file):
    lines = file.readlines()
        
    data = {key: [] for key in lines[0].strip().split(',')}
    
    lines = lines[1:]
    
    for line in lines:
        line = line.strip()
        line_data = line.split(',')
        for index, key in enumerate(data):
            if all((char in "-0123456789." for char in line_data[index])) and my_len((char for char in line_data[index] if char == '-')) <= 1:
                data[key].append(float(line_data[index]) if line_data[index] else 0)
            else:
                data[key].append(line_data[index])
    return data

def parse_file_data_by_house(file_data):
    data = {
        "Slytherin": [],
        "Ravenclaw": [],
        "Gryffindor": [],
        "Hufflepuff": [],
    }
    # print(file_data["Astronomy"])
    for index, house in enumerate(file_data["Hogwarts House"]):
        data[house].append({key: file_data[key][index] for key in file_data if key != "Index" and isinstance(file_data[key][0], float)})
    return data

def get_houses_std_value(house_data):
    mean_data = {key: 0 for key in house_data[0]}
    
    for value in house_data:
        for key in value:
            mean_data[key] += value[key]
    
    for key in mean_data:
        mean_data[key] /= my_len(house_data)
    return mean_data