import sys
import os

if len(sys.argv) < 2:
    print("Need arg.")
else:
    if not os.path.isfile(sys.argv[1]):
        print("File not found.")
    else:
        DATASET_PATH = sys.argv[1]
        f = open(DATASET_PATH, 'r')

        f.readlines()

        

