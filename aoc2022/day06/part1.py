X = [l.strip() for l in open("input.txt")]
X = X[0]

test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz' 
test2 = 'nppdvjthqldpwncqszvftbrmjlhg' 
test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def is_marker(sliced):
    chars = 0
    for t in sliced:
        if sliced.count(t) > 1:
            return False 
        elif sliced.count(t) == 1:
            chars += 1 
    if chars == 4:
        return True

if __name__ == "__main__":

    first_char = False 
    for start in range(0, len(X)):
        stop = start + 4
        marker = X[ start : stop ]
        first_char = is_marker(marker)
        if first_char: 
            print(f"{stop}")    
            break
        marker = []