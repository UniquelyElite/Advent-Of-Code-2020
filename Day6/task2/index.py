#Open and gather the information from a txt file
information = open("./Day6/input.txt")
text = information.read()
lines = text.split("\n")

responses = []
chosen = 0
found = 0
responseAmount = 0
for x in lines :
    if x != '' :
        responseAmount += 1
        for y in x :
            if not y in responses :
                
                responses.append(y)
                found += 1
            else :
                found += 1
    else :
        responses = []
        print(found//responseAmount)
        chosen += found//responseAmount
        found = 0
        responseAmount = 0
print(chosen, 'group "yes" responses')