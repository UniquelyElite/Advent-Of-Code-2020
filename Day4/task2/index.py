#Open and gather the information from a txt file
information = open("./Day4/input.txt")
text = information.read()
lines = text.split("\n")

check = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
alphabet = {'a', 'b', 'c', 'd', 'e', 'f'}
colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
passports = []
correct = 0

#Validation Functions
def numberCheck(min, max, value) :
    if int(value) >= min and int(value) <= max :
        return True
    else :
        return False

def hgt(value) :
    if value[-1] == 'm' and value[-2] == 'c' :
        value = value[:-2]
        if numberCheck(150, 193, value) :
            return True
        else :
            return False
    elif value[-1] == 'n' and value[-2] == 'i' :
        value = value[:-2]
        if numberCheck(59, 76, value) :
            return True
        else :
            return False
    else :
        return False

def hcl(value) :
    if value[0] == '#' and len(value) == 7 :
        value = value[1:]
        for x in value :
            if x in alphabet :
                continue
            try :
                if numberCheck(0, 9, x) :
                    continue
                else :
                    return False
            except :
                return False
        return True
    else :
        return False

def ecl(value) :
    if value in colours :
        return True
    else :
        return False

def pid(value) :
    if len(value) == 9 :
        try :
            for x in value :
                if numberCheck(0, 9, x) :
                    continue
                else :
                    return False
        except :
            return False
        return True

#Seperate passports
passport = ''
passport2 = []
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
        y = y.split(':')
        key = y[0]
        if key in check :
            value = y[1]
            response = False
            #I hate this but couldn't find any other way
            if key == 'byr' :
                response = numberCheck(1920, 2002, value)
            elif key == 'iyr' :
                response = numberCheck(2010, 2020, value)
            elif key == 'eyr' :
                response = numberCheck(2020, 2030, value)
            elif key == 'hgt' :
                response = hgt(value)
            elif key == 'hcl' :
                response = hcl(value)
            elif key == 'ecl' :
                response = ecl(value)
            elif key == 'pid' :
                response = pid(value)
            if response == True :
                true += 1
    if true == 7 :
        passport2.append(x)
        correct += 1
print(passport2)
print(correct, 'is the answer!')