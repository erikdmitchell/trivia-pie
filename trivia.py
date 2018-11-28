
# Import
import json

questions = ''
points = 0
name = 'Steve'

def loadJSONfile():
    global questions

    # get the file and load the json
    questions_json=open('questions.json').read()
    questions = json.loads(questions_json)

def inputName():
    global name

    #name = input("What is your name?")

    print("Welcome,", name)

def runGame():
    outputQuestions()

def outputQuestions():
    global questions

    # loop through questions
    for i in questions["questions"]:
        displayQuestion(i)

def displayQuestion(data):
    global points

    counter = 1
    answer = 0
    totalAnswers = len(data["answers"])
    correctAnswer = data["answer"]

    # output question
    print(data["question"])

    # loop and output answers with identifying number
    for i in data["answers"]:
        print(str(counter) + ".", i) 
        counter = counter + 1

# perhaps this is a while loop?
    # enter answer
    #answer = 2
    #answer = 3

    # validate input
    validateInput(answer, totalAnswers)
# end while loop?
    
    # answer must be subtracted by 1 because array starts at 0
    answer = answer - 1

    if (data["answers"][answer] == correctAnswer):
        points = points + 1

    print(data["answers"][answer])
    print(correctAnswer)
    print(points)

def validateInput(answer, totalAnswers):
    # check is number and is between our range, ie 1-4
    if (1 <= answer <= totalAnswers):
        print("in range")
        # continue
    else:
        print("not in range")
        # ask again for answer

    # return true/false

def main():
    loadJSONfile()
    inputName()
    runGame()

if __name__ == "__main__":
    main()
