#Open and gather the information from a txt file
information = open("./Day3/input.txt")
forest = information.read()
lines = forest.split("\n")

#Get the width of the trees before they repeat
width = len(lines[0])
treeArray = []
path = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
def calculate(right, down) :
    #For location of person
    pinpoint = 0
    treeCount = 0
    line = 0
    for x in lines :
        line += 1
        #check if has reached line yet
        if (line % down == 0 and down % 2 != 0) or (line % down == 1 and down % 2 == 0) :
            #If the person is beyond the trees than correct them
            if pinpoint >= width :
                pinpoint = pinpoint - width
            #Calculate the object in area and check if tree
            y = x[pinpoint]
            if y == '#' :
                treeCount += 1
            #Move dude over
            pinpoint += right
    treeArray.append(treeCount)
answer = 1
for x in path :
    calculate(x[0], x[1])
for x in treeArray :
    answer *= x

print(answer, 'is the number!')