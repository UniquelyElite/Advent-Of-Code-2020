#Open and gather the information from a txt file
information = open("./Day6/input.txt")
text = information.read()
lines = text.split("\n")

#Establish variables
responses = []
chosen = 0
firstLine = True
line = 0

#Loop through every line checking them
for x in lines :
    line += 1
    if x != '' and not line >= len(lines) :
        if firstLine :
            firstLine = False
            for y in x :
                responses.append(y)
            responseCopy = responses
        else :
            new = []
            for y in responses :
                if y in x :
                    new.append(y)
            responses = new
    else :
        firstLine = True
        chosen += len(responses)
        responses = []
        
print(chosen, 'group "yes" responses')