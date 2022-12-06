X = [l.strip() for l in open("input.txt")]
X = X[0]

test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz' 
test2 = 'nppdvjthqldpwncqszvftbrmjlhg' 
test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def is_start_of_packet(sliced):
    chars = 0
    for t in sliced:
        if sliced.count(t) > 1:
            return False 
        elif sliced.count(t) == 1:
            chars += 1 
    if chars == 4:
        return True

def is_start_of_message(sliced):
    chars = 0
    for t in sliced:
        if sliced.count(t) > 1:
            return False 
        elif sliced.count(t) == 1:
            chars += 1 
    if chars == 14:
        return True

if __name__ == "__main__":

    first_char = False 
    for start in range(0, len(X)):
        stop = start + 14
        marker = X[ start : stop ]
        first_char = is_start_of_message(marker)
        if first_char: 
            print(f"{stop}")    
            break
        marker = []
