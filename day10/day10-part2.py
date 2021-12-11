import statistics        
def check_for_corrupt_line(row):
    stack = []
    stack_top = []
    print(row)
    for element in row:
        if element in left_paren:
           stack.append(element)
        if element not in right_paren:
            pass
        else:
            if not stack:
                return False 
            stack_top = stack.pop()
            if stack_top == "\n" or stack_top == " ":
                print("newLine or space")
            if stack_top == '(':
                if element != ")":
                    print(f"element is {element}")
                    return element
                
            if stack_top == '<':
                if element != ">":
                    print(f"element is {element}")
                    return element

            if stack_top == '{':
                if element != "}":
                    print(f"element is {element}")
                    return element

            if stack_top == '[':
                if element != "]":
                    print(f"element is {element}")
                    return element

        
    stack2.append(stack)

    if stack:
        print("calling complete_incomplete")
        process_incomplete(stack2)
        return False
    return True

def process_incomplete(stack2):
    solution = []
    reverse_row = []
    for row in stack2:
        score = 0
        row.reverse()
        for bracket in row:
            if bracket not in left_paren:
                pass
            if bracket == '(':
                score = score * 5 + 1
                reverse_row.append(')') 
            if bracket == '<':
                score = score * 5 + 4
                reverse_row.append('>') 
            if bracket == '{':
                score = score * 5 + 3
                reverse_row.append("}")
            if bracket == '[':
                score = score * 5 + 2
                reverse_row.append(']')
#        print(reverse_row)
        solution.append(score) 
        reverse_row = []
#        print(solution)
#        solution.sort()
#        print(solution)
        row_len = len(solution)
    rjesenje = int(statistics.median(solution))
#        median = int(row_len / 2) 
#    print(solution[median])
    print(rjesenje)

if __name__ == "__main__":

    f1 = open("day10-test.txt", "r")
    f2 = open("day10.txt", "r")
    input_array = []
    right_paren_num_val = {")":3, "]":57, "}":1197, ">":25137}
    left_paren = ["(", "[", "{", "<"]

    right_paren = [")", "]", "}", ">"]
    input_array = f1.readlines()
    stack2 = []
    score = 0
    for element in input_array:
        err = check_for_corrupt_line(element)
        if err == False:
            print("error in stack ")
        elif err == "]":
            score += right_paren_num_val[err]
        elif err == "}":
            score += right_paren_num_val[err]
        elif err == ">":
            score += right_paren_num_val[err]
        elif err == ")":
            score += right_paren_num_val[err]

print(score)



#Part Two


