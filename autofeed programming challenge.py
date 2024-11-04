#Lucas Young
#27/09/2024

#Step 1
def valid_foodweight():
    containerWeight = []
    totalWeight = []
    container = 0

for i in range(5):
    containerWeight = int(input("Please enter the weight of food in each container: "))


while containerWeight < 0 or containerWeight > 200:
    print("Invalid, a single container can only hold up to 200g")
    containerWeight = int(input("Please enter the weight of food in each container: "))
    
containerWeight.append(totalWeight)
totalWeight = totalWeight + containerWeight

#Step 2
def size_dog():
    dogSize = input("Please enter the size of your dog, small, medium or large: ")

#Step 3
def recommended_range():
    if dogSize == "small" and totalWeight > 100 or totalweight < 140:
        range1 = print("This weight of food is suitable for your smalll dog")
    elif dogSize == "medium" and totalweight > 330 or totalweight < 440:
            range1 = print("This weight of food is suitable for your medium dog")
    elif dogSize == "large" and totalweight > 690 or totalweight < 900:
        range1 = print("This weight of food is suitable for your large dog")
    else:
        range1 = print("This weight of food is not recommended for the size of dog")


#Step 4
def average_weight():
    averageWeight = totalWeight / 5
    round.averageWeight(1, 0)


#Step 5
def next_foodWeight():
    for i in range(5):
        print(containerWeight[i])
        print(averageWeight)
        print(totalWeight)
        print(range1)
        

#run the steps





