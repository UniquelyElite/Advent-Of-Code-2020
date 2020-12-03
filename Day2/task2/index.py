#Open and gather the information from a txt file
information = open('./Day2/input.txt')
text = information.read()
numbers = text.split('\n')

#For logging the amount of correct pwds
correct = 0

#The 'algorithm'
for x in numbers :
    info = x.split(' ')
    between = info[0].split('-')
    locate = info[1].split(':')[0]
    pwd = info[2]
    lettersFound = 0
    if pwd[int(between[0]) - 1] == locate :
        lettersFound += 1
    if pwd[int(between[1]) - 1] == locate :
        lettersFound += 1
    if lettersFound == 1 :
        correct += 1

#Print the answer
print(correct, 'found!')