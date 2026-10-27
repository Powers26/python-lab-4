#Lium Powers, Python Programming, 10/__/2026
#This program takes an input from the user and counts how many words are in their input

#countWords will count how many words are in a sentence
def countWords(Phrase):
    #if the user starts the sentence with a space, count will start from 0
    if Phrase[0] != " ":
        count = 1
    else:
        count = 0

    #if the sentence ends with one or multiple spaces, removes them from the end
    while Phrase[-1] == " ":
        Phrase = Phrase[0, len(Phrase) - 1]


    #iterates through the phrase and if it finds a singular space, adds to count
    for i in range(len(Phrase)):
        if Phrase[i] == " " and Phrase[i + 1] != " ":
            count = count + 1
        

    return count

#requests user input
print("Please input a sentence.")
sentence = input()

#prints result of the count words function with the input phrase
print("There are " + str(countWords(sentence)) + " words!")