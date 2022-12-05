X = [l.strip().split() for l in open("input.txt")]
#X = [l.strip().split() for l in open("input_t.txt")]
# move {how many} from queue X to queue y
dict_ = {"Q1" : ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
"Q2" : ['D', 'W', 'B'], 
"Q3" : ['T', 'S', 'Q', 'W', 'J', 'C'],
"Q4" : ['F', 'J', 'R', 'N', 'Z', 'T', 'P'], 
"Q5" : ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
"Q6" : ['B', 'W', 'F', 'T', 'N'],
"Q7" : ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
"Q8" : ['H', 'P', 'F', 'R'], 
"Q9" : ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H'], 
         }
dict_t = {

          "Q1": ['Z', 'N'],
          "Q2": ['M', 'C', 'D'],
          "Q3": ['P'],

          }
Y = []

queues_1 = { '1': 'Q1', '2': 'Q2', '3': 'Q3', '4': 'Q4', '5': 'Q5', '6':'Q6', '7': 'Q7', '8': 'Q8', '9':'Q9'} 
for i in X:
    Y.append(i)

if __name__ == '__main__':
    answ = ''
    for i in Y:
        how_many = int(i[1])
        from_ = "Q" +i[3]
        to_ = "Q" + i[5]
        for i in range(how_many):
            a = dict_[from_].pop()
            dict_[to_].append(a)
#            a = dict_t[from_].pop()
#            dict_t[to_].append(a)
    for k, v in dict_.items():
       answ += v[-1]
    print(answ)
