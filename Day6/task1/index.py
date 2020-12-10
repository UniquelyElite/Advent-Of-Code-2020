#Open and gather the information from a txt file
information = open("./Day6/input.txt")
text = information.read()
lines = text.split("\n")

responses = []
chosen = 0
for x in lines :
    if x != '' :
        for y in x :
            if not y in responses :
                responses.append(y)
                chosen += 1
    else :
        responses = []
print(chosen, '"yes" responses')