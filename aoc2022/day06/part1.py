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
    #    print(len(X[0]))
    #print(X[0], X[4094])
    #for i in range(len(X) - 1):
        #marker = X[ i : i + 4 ]
        #print(find_marker(marker))

    first_char = False 
    for start in range(0, len(X)):
        #        print(f"Array len = {len(test3)}")
        stop = start + 4
        marker = X[ start : stop ]
        #print(marker)
        first_char = is_marker(marker)
        #print(f"start {start} stop {stop}")
        if first_char: 
            print(f"{stop}")    
            break
        marker = []
