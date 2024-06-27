import os
import sys
from Utils.file_utils import get_houses_mean_value, open_file, parse_file, parse_file_data_by_house
from Utils.my_math import my_len, my_sum
import matplotlib.pyplot as plt


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
            
            print(sum(file_data['Arithmancy']) / len(file_data['Arithmancy']))
            
            gryffindor_data = get_houses_mean_value(houses_data["Gryffindor"])
            ravenclaw_data = get_houses_mean_value(houses_data["Ravenclaw"])
            slytherin_data = get_houses_mean_value(houses_data["Slytherin"])
            hufflepuff_data = get_houses_mean_value(houses_data["Hufflepuff"])
            
            
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
            fig.suptitle('Courses grade for each Houses')

            ax1.plot([key for key in gryffindor_data], [gryffindor_data[key] for key in gryffindor_data] )
            ax1.tick_params(axis='x', labelrotation=90)

            ax2.plot([key for key in ravenclaw_data], [ravenclaw_data[key] for key in ravenclaw_data] )
            ax2.tick_params(axis='x', labelrotation=90)

            ax3.plot([key for key in slytherin_data], [slytherin_data[key] for key in slytherin_data] )
            ax3.tick_params(axis='x', labelrotation=90)

            ax4.plot([key for key in hufflepuff_data], [hufflepuff_data[key] for key in hufflepuff_data] )
            ax4.tick_params(axis='x', labelrotation=90)

            plt.show()
            

            
            