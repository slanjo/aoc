import sys
from collections import defaultdict, Counter
from itertools import permutations

DIGITS = []

def sortString(string):
    return(''.join(sorted(string)))

def unionCheck(test, four, eight):
    temp = []
    for i in four:
        temp.append(i)
    for k in test:
        if k in temp:
            continue 
        else:
            temp.append(k)
    temp_str = sortString(''.join(temp))
    if temp_str == eight:
        return True
    else:
        return False
                 

if __name__ == '__main__':
    r_enc = []
    l_enc = []
    row_total = ''
    f = sys.argv[1] if len(sys.argv) > 1 else '8.in'
    for line in open(f, "r"):
        before, after = line.split("|")
#       r_enc.append(after.strip().split())
        r_enc.append(after.split())
        l_enc.append(before.split())

    row_template_dict = {}
    counter4 = 0
    counter1 = 0
    counter = 0
    for row in l_enc:
        single_digit = 0
#Alocate known digits to their correspoding keys 
        row.sort(key=len)
        row_template_dict[1] = sortString(row[0])
        row_template_dict[4] = sortString(row[2])
        row_template_dict[7] = sortString(row[1])
        row_template_dict[8] = sortString(row[-1])
#examine every row for digits
        for col in row:
            sorted_col = sortString(col)
            len_sorted_col = len(sorted_col)
#****************************************
#if len==6 and if digit contains both segments of a '1' (it is not a '6')
#   if digit contains '4' it is a '9'
#   else digit is a '0'
#else digit is a '6' 
            if len_sorted_col == 6: 
                temp = sorted(sorted_col)
                for k in row_template_dict[1]:
                    if k in sorted_col:
                        counter1+=1
                if counter1 == 2:
                    for i in row_template_dict[4]:
                        if i in sorted_col:
                            counter4+=1 
                    if counter4 == 4:
                        row_template_dict[9] = sorted_col
                    else:
                        row_template_dict[0] = sorted_col
                else:
                    row_template_dict[6] = sorted_col 
                counter4 = 0
                counter1 = 0

#****************************************
#if len==5 and if digit contains a '1' digit is a '3'
#elif union of '4' is '8' digit is a '2'
#else digit of len 5 is a 5
            if len_sorted_col == 5:  
                for k in row_template_dict[1]:
                    if k in sorted_col:
                        counter1 += 1
                if counter1 == 2:
                    row_template_dict[3] = sorted_col
                elif  unionCheck(sorted_col, row_template_dict[4], row_template_dict[8]): 
                    row_template_dict[2] = sorted_col 
                else:
                    row_template_dict[5] = sorted_col
            counter1 = 0
        for digit in r_enc[counter]:
            single_digit_=sortString(digit)
            for key, val in row_template_dict.items():
                if single_digit_ == val:
                    row_total+=str(key)
        DIGITS.append(int(row_total))
        row_total = ''
        counter+=1
    print(sum(DIGITS))
