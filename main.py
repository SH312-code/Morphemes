import random
def read_file(filename):#This function reads a file and extracts the data as a list seperated by the lines in the flies. 
    with open(filename, "r") as f:
        return f.read().splitlines()
score = 0

data = read_file("morphemes.txt")
q = []
defintions = []
terms = []
for i in range((len(data) - 1)):
    if i % 2 == 0:
        terms.append(data[i])
    else:
        defintions.append(data[i])
for i in range(len(terms)-1):
    q.append([terms[i], defintions[i]])

random.shuffle(q)

for i in range(len(q)-1):
    ask = input("Define " + q[i][0])
    if ask.upper() == (q[i][1]).upper():
        print("Correct")
        score += 1
    else:
        print("Sorry the correct answer was " + q[i][1])
    print()
x = len(q)
print("You got "+str(score) + " out of " + str(x) + " correct")