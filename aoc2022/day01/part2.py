

if __name__ == "__main__":

    elf_kcal_raw = []
    elf_kcal = []
    max_elf_kcal = 0
    max_elf_kcal_run = 0
    top_three = [0, 0, 0]

    with open("input.txt", "r") as f:
        elf_kcal_raw = f.readlines()
        for food in elf_kcal_raw:
            elf_kcal.append(food.strip('\n'))
    for kcal in elf_kcal:
        if kcal == '': 
            if max_elf_kcal_run > top_three[2]:
                if max_elf_kcal_run > top_three[1]:
                    if max_elf_kcal_run > top_three[0]:
                        top_three[2] = top_three[1]
                        top_three[1] = top_three[0]
                        top_three[0] = max_elf_kcal_run
                    else: 
                        top_three[2] = top_three[1]
                        top_three[1] = max_elf_kcal_run
                else:
                    top_three[2] = max_elf_kcal_run

            max_elf_kcal_run = 0
        else:
            max_elf_kcal_run += int(kcal)
#    print(f"max cal elf --> {max_elf_kcal}")
#    print(f"max cal elf array --> {top_three[0]}")
#    print(f"top three ==> {sum(top_three)}")
#    print(top_three)
    print(sum(top_three))
    
