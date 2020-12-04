#Open and gather the information from a txt file
information = open("./Day3/input.txt")
forest = information.read()
lines = forest.split("\n")

#Get the width of the trees before they repeat
width = len(lines[0])

#For location of person
pinpoint = 0
treeCount = 0

for x in lines :
    #If the person is beyond the trees than correct them
    if pinpoint >= width :
        pinpoint = pinpoint - width
    #Calculate the object in area and check if tree
    y = x[pinpoint]
    if y == '#' :
        treeCount += 1
    #Move dude over three
    pinpoint += 3

print(treeCount)