#Open and gather the information from a txt file
information = open("./Day4/input.txt")
text = information.read()
lines = text.split("\n")

check = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passports = []
correct = 0

#Seperate passports
passport = ''
line = 0
for x in lines :
    line += 1
    if x != '' :
        passport += (x + ' ')
    if x == '' or len(lines) == line :
        passport[:-1]
        passports.append(passport)
        passport = ''
#Check passports
for x in passports :
    x = x.split(' ')
    true = 0
    for y in x :
        y = y.split(':')[0]
        if y in check :
            true += 1
    if true == 7 :
        correct += 1
print(correct)