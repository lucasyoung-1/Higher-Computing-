import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = "C:\Users\fafay\OneDrive\Desktop\Python"

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath+'ufo_sighting.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----
def CountSightings(country, specifiedCountry):
    numSightings = 0
    for index in range(0,len(country)):
        if country[index] == specifiedCountry:
            numSightings = numSightings + 1

    return numSightings


def DisplaySightings(specifiedCountry, numSightings):
    print(specifiedCountry, numSightings)
    pass

def CountYearSightings(thisDate, specifiedyear):
    yearsightings = 0
    for index in range(0, len(thisDate)):
        if thisDate[index] == specifiedyear:
            yearsightings = yearsightings + 1
            return yearsightings, specifiedyear

def displayyearlysightings(yearsightings, thisDate):
    print(thisDate, yearsightings)
    pass

#main program 
thisDate, country, location, shape, description = importFile()
specifiedCountry = "England"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Scotland"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Wales"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Northern Ireland"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedyear = thisDate[0]
yearsightings = CountYearSightings(thisDate, specifiedyear)
displayyearlysightings(specifiedyear, yearsightings)
