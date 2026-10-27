#Lium Powers, Python Lab 4, 10/29/2026

#takes two lists and makes a dictionary of names and scores
def makeDictionary(Name, Score):
    newDict = {}
    for i in range(len(Name)):
        newDict[Name[i]] = Score[i]

    return(newDict)

def scoreAverage(list):
    sum = 0
    for i in range (len(list)):
        sum = sum + list[i]

    return(sum/4.0)

Students = ['Joe', 'Tom', 'Barb', 'Sue', 'Sally']
Scores = [10, 23, 13, 18, 12]

scoreDict = makeDictionary(Students, Scores)
print(scoreDict)

#prints only barb's score
print(scoreDict['Barb'])

#adds new key and value to dictionary
scoreDict['John'] = 19

print(scoreDict)

#creates a list that has the values of each score
scoreList = []
for i in scoreDict:
    scoreList.append(scoreDict[i])

#sorts the scores
scoreList.sort()
print(scoreList)

#gets the average and score and prints it
print("Average score is: ", scoreAverage(scoreList))

#changes sally's score
scoreDict['Sally'] = 13

#removes tom
del scoreDict['Tom']
print(scoreDict)