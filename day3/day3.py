f = open("day3-in.txt", "r")
#f = open("day3-test-in.txt", "r")

lista = f.readlines()
f.close()
zeros = 0
column_0 = [0,0,0,0,0,0,0,0,0,0,0,0]
column_1 = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ""
epsilon = ""

for red in lista:
    for i in range (0, len(red) - 1):
        if red[i] == "0":
            column_0[i] += 1
        elif red[i] == "1":
            column_1[i] += 1

for k in range(0, 12):
    if column_0[k] > column_1[k]:
        gamma += "0"
        epsilon += "1"
    elif column_1[k] > column_0[k]:
        gamma += "1"
        epsilon += "0"

binary_converted_gamma = ' '.join(map(bin, bytearray(gamma, "utf-8")))        
binary_converted_epsilon = ' '.join(map(bin, bytearray(epsilon, "utf-8")))        
dec_gamma = int(gamma, 2)
dec_epsilon = int(epsilon, 2)

print(column_0) 
print(column_1)
print(gamma, epsilon)
print(dec_gamma, dec_epsilon)
print(dec_epsilon * dec_gamma)
### Part two ####
print("\n\n\n\n*********************PART TWO ******************")
def check_position_count(remaining_list, position, operacija):
    kolona_0 = 0
    kolona_1 = 0

    for row in remaining_list:
        if row[position] == "0":
            kolona_0 += 1
        elif row[position] == "1":
            kolona_1 += 1

    if kolona_0 > kolona_1:
        if operacija == "o2":
            return 0 #more zeroes 
        else:
            return 1 #more ones 
    elif kolona_0 < kolona_1:
        if operacija == "o2":
            return 1
        else:
            return 0
    elif kolona_0 == kolona_1:
        if operacija == "o2":
            return 2
        else:
            return 2


lista_gen_rate = lista[:]
co2_scrubber = lista[:]
#h = 0
duzina_liste = len(lista)
pozicija = 0
row_num = 0
# **************************** OXYGEN GENERATOR **********************
while duzina_liste >= 1:
    if pozicija < 12:    
        operacija = "o2"
        position_status = check_position_count(lista_gen_rate, pozicija, operacija) 
        if position_status == 2:
            row_num = 0
            duzina_liste = len(lista_gen_rate)
            while row_num < duzina_liste:
                if int(lista_gen_rate[row_num][pozicija]) == 0:
                    lista_gen_rate.pop(row_num)
                    duzina_liste = len(lista_gen_rate)
                    row_num = 0
                else: 
                    row_num += 1

        elif position_status == 1:
            row_num = 0
            duzina_liste = len(lista_gen_rate)
            while row_num < duzina_liste:
                if int(lista_gen_rate[row_num][pozicija]) == 0: 
                    lista_gen_rate.pop(row_num)
                    duzina_liste = len(lista_gen_rate)
                    row_num = 0
                else:
                    row_num += 1

        else: #position_status == 0:
            row_num = 0
            duzina_liste = len(lista_gen_rate)
            while row_num < duzina_liste:
                if int(lista_gen_rate[row_num][pozicija]) == 1:
                    lista_gen_rate.pop(row_num)
                    duzina_liste = len(lista_gen_rate)
                    row_num = 0 
                else: 
                    row_num += 1
    pozicija += 1
    duzina_liste -= 1

# **************** CO2 SCRUBBER **************************
duzina_scrub = len(lista)
pozicija = 0
row_num = 0

while duzina_scrub >= 1:
    if pozicija < 12:    
        operacija = "co2"
        position_status = check_position_count(co2_scrubber, pozicija, operacija) 
        if position_status == 2:
            row_num = 0
            duzina_scrub = len(co2_scrubber)
            while row_num < duzina_scrub:
                if int(co2_scrubber[row_num][pozicija]) == 1:
                    co2_scrubber.pop(row_num)
                    duzina_scrub = len(co2_scrubber)
                    row_num = 0
                else: 
                    row_num += 1

        elif position_status == 1:
            row_num = 0
            duzina_scrub = len(co2_scrubber)
            while row_num < duzina_scrub:
                if int(co2_scrubber[row_num][pozicija]) == 0: 
                    co2_scrubber.pop(row_num)
                    duzina_scrub = len(co2_scrubber)
                    row_num = 0
                else:
                    row_num += 1

        else: #position_status == 0:
            row_num = 0
            duzina_scrub = len(co2_scrubber)
            while row_num < duzina_scrub:
                if int(co2_scrubber[row_num][pozicija]) == 1:
                    co2_scrubber.pop(row_num)
                    duzina_scrub = len(co2_scrubber)
                    row_num = 0 
                else: 
                    row_num += 1
    pozicija += 1
    duzina_scrub -= 1

print(lista_gen_rate)
print(co2_scrubber)

print(f"{int(lista_gen_rate[0], 2) * int(co2_scrubber[0],2)}")
#oxygen_gen_rating = most common value in the current bit position
#co2_scrub = least common value in the current bit position