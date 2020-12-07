#Open and gather the information from a txt file
information = open("./Day5/input.txt")
text = information.read()
lines = text.split("\n")

lowest = None
highest = None
seats = []

#Sort the seats out
for x in lines :
    currentNumber = [0, 128]
    frontBack = ''
    leftRight = ''
    for y in x :
        if y == 'F' or y == 'B' :
            frontBack += y
        else :
            leftRight += y
    for y in frontBack :
        if y == 'F' :
            #yes i can do meth
            currentNumber[1] = currentNumber[1]/2 + currentNumber[0]/2
        else :
            #maf*
            currentNumber[0] = currentNumber[1]/2 + currentNumber[0]/2
    row = currentNumber[0]
    currentNumber = [0, 8]
    for y in leftRight :
        if y == 'L' :
            #math** there we go
            currentNumber[1] = currentNumber[1]/2 + currentNumber[0]/2
        else :
            #Surprised the same math still works-
            currentNumber[0] = currentNumber[1]/2 + currentNumber[0]/2
    column = currentNumber[0]
    seatID = row * 8 + column
    seats.append(seatID)
    try :
        if seatID > highest :
            highest = seatID
    except :
        highest = seatID
    try :
        if seatID < lowest :
            lowest = seatID
    except :
        lowest = seatID
#Pinpoint empty seats
x = lowest
openSeats = []
while not x > highest :
    found = False
    for y in seats :
        if y == x :
            found = True
    if found == False :
        openSeats.append(x)
    x += 1
print('The seat(s) with the ID of', openSeats, 'were found to be open!')