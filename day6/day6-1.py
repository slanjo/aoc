
"""
    every time we enter the loop we:
        check if lanternfish internaltimer==0:
            set that lanterfish internaltimer to 6
            create a new lantern fish and set its internaltimer to 8 -- append 8 to the end of list

"""
from ulaz import test_input, input, sat1_input
from collections import OrderedDict
START_SCHOOL = OrderedDict()

def model_lanternfish(NEW_SCHOOL):

    for lanternfish in list(NEW_SCHOOL.keys()):
        if NEW_SCHOOL[lanternfish] >= 0:
            NEW_SCHOOL[lanternfish] -= 1  
        if NEW_SCHOOL[lanternfish] == -1:
            NEW_SCHOOL[lanternfish]  = 6
            NEW_SCHOOL[(len(NEW_SCHOOL) + 1)] = 8
    START_SCHOOL = NEW_SCHOOL

if __name__ == '__main__':
#    print(test_input)
    print(f"Length of input: {len(input)}")
#   sat2 = input 
    sat2 = test_input
    duzina = len(sat2)

    START_SCHOOL = { lantern_fish : sat2[lantern_fish] for lantern_fish in range(0, duzina)}
    NEW_SCHOOL = START_SCHOOL
#   print(sat2)
    day = 0 
    while(day < 80):
        model_lanternfish(NEW_SCHOOL)
        day += 1 

#   for key, value in START_SCHOOL.items():
#       print(f"{key} -> {value}")

    print(f"Number of fish in lantern school: {len(START_SCHOOL)}")
