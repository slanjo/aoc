from os import EX_UNAVAILABLE


f1 = open("day10-test.txt", "r")
f2 = open("day10.txt", "r")
input_array = []
right_paren_num_val = {")":3, "]":57, "}":1197, ">":25137}
left_paren = ["(", "[", "{", "<"]
input_array = f2.readlines()

def check_for_failed_bracket(row):

    stack = []
    
    for element in row:
        if element in left_paren:
           stack.append(element)
        else:

            if not stack:
                return False 
            current_char = stack.pop()
            if current_char == '(':
                if element != ")":
                    return element
                
            if current_char == '<':
                if element != ">":
                    return element

            if current_char == '{':
                if element != "}":
                    return element

            if current_char == '[':
                if element != "]":
                    return element
    if stack:
        print(stack)
        return False
    return True


if __name__ == "__main__":
    score = 0
    for element in input_array:
        err = check_for_failed_bracket(element)
        if err == False:
            print("No errors ")
        elif err == "]":
            score += right_paren_num_val[err]
        elif err == "}":
            score += right_paren_num_val[err]
        elif err == ">":
            score += right_paren_num_val[err]
        elif err == ")":
            score += right_paren_num_val[err]
print(score)