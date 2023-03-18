# Code for generating compression demo data sets
# 
#
# Author: Josh McIntyre
#
import random

import names

FILENAME = "uncompressed.txt"
ENTRIES = 100
OPTIONS = [ "white belt", "blue belt", "purple belt", "brown belt", "black belt" ]

def main():

    with open(FILENAME, "w") as f:
        for i in range(0, ENTRIES):
            gender = random.choice(["male", "female"])
            name = names.get_full_name(gender=gender)
            belt = random.choice(OPTIONS)
            
            entry = f"{name}\t{belt}\n"
            f.write(entry)
            
            
if __name__ == main():
    main()
