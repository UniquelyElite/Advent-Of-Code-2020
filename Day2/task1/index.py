#Open and gather the information from a txt file
information = open('./Day2/input.txt')
text = information.read()
numbers = text.split('\n')

#For logging the amount of correct pwds
correct = 0

#The 'algorithm' (totally doesnt just brute force it LMFAO)
for x in numbers :
    info = x.split(' ')
    between = info[0].split('-')
    locate = info[1].split(':')[0]
    pwd = info[2]
    lettersFound = 0
    for y in pwd :
        if y == locate :
            lettersFound += 1
    if lettersFound >= int(between[0]) and lettersFound <= int(between[1]) :
        correct += 1

#Print the answer
print(correct, 'found!')