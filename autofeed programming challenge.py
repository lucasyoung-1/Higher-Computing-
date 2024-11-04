#Lucas Young
#27/09/2024

#Step 1
def valid_foodweight():
    containerWeights = []
    totalWeight = 0
    container = 0

    for i in range(5):
        containerWeight = int(input("Please enter the weight of food in each container: "))


        while containerWeight < 0 or containerWeight > 200:
            print("Invalid, a single container can only hold up to 200g")
            containerWeight = int(input("Please enter the weight of food in each container: "))
        
        containerWeights.append(totalWeight)
        totalWeight = totalWeight + containerWeight
    return totalWeight, containerWeights

#Step 2
def size_dog():
    dogSize = input("Please enter the size of your dog, small, medium or large: ")
    return dogSize

#Step 3
def recommended_range(dogSize, totalWeight):
    if dogSize == "small" and totalWeight > 100 or totalWeight < 140:
        range1 = "This weight of food is suitable for your small dog"
    elif dogSize == "medium" and totalWeight > 330 or totalWeight < 440:
            range1 = "This weight of food is suitable for your medium dog"
    elif dogSize == "large" and totalWeight > 690 or totalWeight < 900:
        range1 = "This weight of food is suitable for your large dog"
    else:
        range1 = "This weight of food is not recommended for the size of dog"
    return range1

#Step 4
def average_weight(totalWeight):
    averageWeight = totalWeight / 5
    averageWeight = round(averageWeight,1)
    return averageWeight

#Step 5
def next_foodWeight(containerWeight, averageWeight, totalWeight, range1):
    for i in range(5):
        print(containerWeight[i])
        print(averageWeight)
        print(totalWeight)
        print(range1)

#run the steps
tW, cW = valid_foodweight()
dS = size_dog()
r1 = recommended_range(dS, tW)
aW = average_weight(tW)
next_foodWeight(cW, aW, tW, r1)







