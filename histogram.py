import os
import sys
from Utils.file_utils import get_houses_std_value, open_file, parse_file, parse_file_data_by_house
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
            
            gryffindor_data = get_houses_std_value(houses_data["Gryffindor"])
            ravenclaw_data = get_houses_std_value(houses_data["Ravenclaw"])
            slytherin_data = get_houses_std_value(houses_data["Slytherin"])
            hufflepuff_data = get_houses_std_value(houses_data["Hufflepuff"])
            
            
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
            fig.suptitle('Courses grade for each Houses')

            ax1.plot([key.split(' ')[0] for key in gryffindor_data], [gryffindor_data[key] for key in gryffindor_data], color='red' )
            ax1.tick_params(axis='x', labelrotation=90)
            ax1.set_title("Gryffindor Std Courses Grade")

            ax2.plot([key.split(' ')[0] for key in ravenclaw_data], [ravenclaw_data[key] for key in ravenclaw_data], color='blue' )
            ax2.tick_params(axis='x', labelrotation=90)
            ax2.set_title("Ravenclaw Std Courses Grade")

            ax3.plot([key.split(' ')[0] for key in slytherin_data], [slytherin_data[key] for key in slytherin_data], color='green' )
            ax3.tick_params(axis='x', labelrotation=90)
            ax3.set_title("Slytherin Std Courses Grade")

            ax4.plot([key.split(' ')[0] for key in hufflepuff_data], [hufflepuff_data[key] for key in hufflepuff_data], color='yellow' )
            ax4.tick_params(axis='x', labelrotation=90)
            ax4.set_title("Hufflepuff Std Courses Grade")

            plt.show()


            
            