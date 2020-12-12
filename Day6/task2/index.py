#Open and gather the information from a txt file
information = open("./Day6/input.txt")
text = information.read()
lines = text.split("\n")

responses = []
chosen = 0
firstLine = True
line = 0

for x in lines :
    line += 1
    if x != '' and not line >= len(lines) :
        if firstLine :
            firstLine = False
            for y in x :
                responses.append(y)
        else :
            for y in responses :
                if not y in x :
                    responses.remove(y)
    else :
        firstLine = True
        chosen += len(responses)
        responses = []
print(chosen, 'group "yes" responses')