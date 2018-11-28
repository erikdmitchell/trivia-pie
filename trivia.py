
# Import
import json

questions = ''
points = 0
name = 'Steve'
def loadQuestions():
    global questions

    questions = loadJSONfile('questions.json')

def loadJSONfile(filename):
    global questions

    # get the file and load the json
    json_data = open(filename).read()

    return json.loads(json_data)

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

    # end game
    endGame()

def displayQuestion(data):
    global points

    counter = 1
    answer = 2 #default to 0
    totalAnswers = len(data["answers"])
    correctAnswer = data["answer"]
    validInput = False

    # output question
    print(data["question"])

    # loop and output answers with identifying number
    for i in data["answers"]:
        print(str(counter) + ".", i) 
        counter = counter + 1

    # loop until we have a valid answer
    while True:
        print("input answer")
        validInput = validateInput(answer, totalAnswers)

        if validInput == True:
            break
    
    # answer must be subtracted by 1 because array starts at 0
    answer = answer - 1

    # if answer is correct, add points
    if (data["answers"][answer] == correctAnswer):
        points = points + 1

def validateInput(answer, totalAnswers):
    # check is number and is between our range
    if (1 <= answer <= totalAnswers):
        return True

    return False

def endGame():
    global name, points

    print("Congratualtions, " + str(name) + "! You have " + str(points) + " points." )

    updateHighScores(name, points)
    displayHighScores()

def updateHighScores(name, points):
    # load high scores
    highScoresData = loadJSONfile('highscores.json')

    # add to json
    # highScoresData["scores"].append({
    #     "name": name,
    #     "points": points
    # })
    
    # double sort, first by name, then points
    highScoresData["scores"] = sorted(highScoresData["scores"], key=lambda i : i['name'])
    highScoresData["scores"] = sorted(highScoresData["scores"], key=lambda i : i['points'], reverse=True)

    # write to file
    with open("highscores.json", "w") as outfile:
        json.dump(highScoresData, outfile, indent=4)

def displayHighScores():
    print("high scores here:")

def main():
    loadQuestions()
    inputName()
    runGame()

if __name__ == "__main__":
    main()
