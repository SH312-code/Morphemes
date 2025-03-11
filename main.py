import random
def read_file(filename):#This function reads a file and extracts the data as a list seperated by the lines in the flies. 
    with open(filename, "r") as f:
        return f.read().splitlines()

data = read_file("morphemes.txt")
wrong =[]
def data_collect(info: list):
    defintions = []
    terms = []
    q = []
    for i in range((len(info))):
        if i % 2 == 0:
            root = info[i] + " "
            terms.append(root)
        else:
            defintions.append(info[i])
    for i in range(len(terms)):
        q.append([terms[i], defintions[i]])
    return q
space = ' '
def quiz(list: list):
    wrong = []
    for i in range(len(list)):
        question = list[i-1]
        to_ask = question[0]
        answer = question[1].upper()
        answer = str(answer).split(',')
        ask = input("Define " + str(to_ask)).upper()
        if ask == space.join(answer):
            print("Correct")
        elif ask in answer:
            print(f"Half right all are listed, {str(answer)}")
        else:
            print(f"Sorry the correct answer was {str(answer)}")
            while True:
                try:
                    incorrect = input("Did you get this wrong? (Yes/No)")
                    if incorrect.upper() in ['YES', 'NO']:
                        if incorrect.upper() == 'YES':
                            for word in question:
                                wrong.append(word)
                            print("Question marked for review")
                        else:
                            print("k")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid")
        print()
def after():
    retry_all =bool(input("Would you like to retry the entire quiz?(Leave blank if no) "))
    if retry_all:
        quiz()
        after()
    else:
        retry_wrong = bool(input("Would you like to retry the questions you got wrong (Leave blank if no) "))
        if retry_wrong:
            quiz(data_collect(wrong))
            after()
        else:
            print("Thanks")
            quit()
def test_case():
    counter = 1
    for i in data_collect(data):
        print(counter, i)
        counter +=1
def full_run():
    start_words = data_collect(data)
    random.shuffle(start_words)
    quiz(start_words)
    after()

full_run()
#test_case()
