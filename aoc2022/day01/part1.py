

if __name__ == "__main__":

    elf_kcal_raw = []
    elf_kcal = []
    max_elf_kcal = 0
    max_elf_kcal_run = 0

    with open("input.txt", "r") as f:
        elf_kcal_raw = f.readlines()
        for food in elf_kcal_raw:
            elf_kcal.append(food.strip('\n'))
    for kcal in elf_kcal:
        if kcal == '': 
            if max_elf_kcal_run > max_elf_kcal:
                max_elf_kcal = max_elf_kcal_run
            max_elf_kcal_run = 0

        else:
            max_elf_kcal_run += int(kcal)
    print(max_elf_kcal)

    
