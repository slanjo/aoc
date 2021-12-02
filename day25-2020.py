##### 2020 Day 25 Part 1 #####
card_pk = 0
door_pk = 0
value = 1
counter_card = 0
counter_door = 0

while card_pk != 2084668:
    value *= 7 
    value = value % 20201227
    card_pk = value
    counter_card += 1 

value = 1
while door_pk != 3704642:
    value *= 7 
    value = value % 20201227
    door_pk = value
    counter_door += 1 

value = 1
for i in range(0, counter_card):
    value *= door_pk 
    value = value % 20201227
    door_crypto = value

value = 1     
for i in range(0, counter_door):
    value *= card_pk 
    value = value % 20201227
    card_crypto = value

print(f"Door Loop ---> {counter_door}\nDoor PK ---> {door_pk}\nCard Loop ---> {counter_card}\nCard PK ---> {card_pk}")
print(f"Door crypto ---> {door_crypto}\nCard crypto --> {card_crypto}")