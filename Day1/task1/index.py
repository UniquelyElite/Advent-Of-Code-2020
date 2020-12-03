#Open and gather the information from a txt file
information = open("./Day1/input.txt")
text = information.read()
numbers = text.split("\n")

#Run it through a loop that checks each number for each number to see if they match the criteria, will log the answer
for x in numbers :
    x = int(x)
    for y in numbers :
        y = int(y)
        z = x + y
        if z == 2020 :
            z = x * y
            print(z, 'is the number!')
            exit()