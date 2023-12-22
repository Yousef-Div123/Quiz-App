from random import randint

class Question():
    def __init__(self, body, choices, answer):
        self._body = body
        self._choices = choices
        self._answer = answer 
        
    def getChoices(self):
        # this method should return a list of choices in random order(don't modify the existing choices list)
        newChoices = []
        tempList = list(self._choices)
        
        # this for loop get a random choice from templist then add it to newChoices then remove the choice from templist
        for i in range(3, -1, -1):
            num = randint(0,i) # i throught the loop is [3, 2, 1, 0]
            newChoices.append(tempList[num])
            tempList.remove(tempList[num])
            
        return newChoices
        
    def isCorrect(self, userAnswer):
        if userAnswer == self._answer:
            return True
        else:
            return False
    
    def getBody(self):
        return self._body
    
    def getAnswer(self):
        return self._answer
    
    

def readQustions(fileName):
    # this function should read questions from the questions.txt and return a list of Question objects        
    file  = open(fileName, 'r')
    lines = file.readlines()
    
    #removing \n from the end of each line
    i = 0
    for line in lines:
        lines[i] = line.rstrip()
        i+=1
    
    questions = [] 
    
    # the question body and the choices and the answers are 6 lines
    for i in range(0, len(lines), 6):# a loop that add 6 each time [0, 6, 12, ....]
        body = lines[i] # the first line is the body
        choices = lines[i + 1:i + 5] # lines from the second to the fifth are choices
        answer = lines[i + 5] # the last line is the answer
        question = Question(body, choices, answer)
        questions.append(question) # adding the question object to questions list
    

    file.close()
    return questions
    
def writeAnswers(quiz):
    # this function will read a list of dictionaries. Each dictionary contain a question and an answer.
    # It should write the questions and answers to answers.txt as shown in the output
    file = open('answers.txt', 'w')
    for question in quiz:
        # each question dictionary in this loop is like this {'question': question object, 'userAnswer': answer, 'questionNum' : questionsNum }
        body = question['question'].getBody()
        correctAnswer = question['question'].getAnswer()
        file.write(f"Question #{question['questionNum']}: {body}\n")
        file.write(f"Your Answer: {question['userAnswer']}\n")
        file.write(f"Correct Answer: {correctAnswer}\n\n") # double \n because we want an empty line between each question
        
    file.close()



def getValidInput():
    while True: # the loop only stops if the function return something
        answer = input("Enter your choice (number) or 'Q' to quit: ")
        if answer.isdigit(): # checking if the answer is an integer
            if 4>= int(answer) >= 1:
                return answer
        else:
            # if the answer is not an integer, it is either a q to quite or an invalid input
            if answer.upper() == 'Q': # taking q.upper so it is not case sensitve
                return answer.upper()
        print('\nInvalid input. Please try again.') # if the function doesn't return anything in the end of the loop then it is an invalid input
            
def getScore(score, questionsNum):
    if questionsNum != 0: # the user didn't answer any question we don't want to get division by zero error
        return (score/questionsNum) * 100
    else:
        return 0.0

    
def main():
    questions = readQustions('questions.txt') # getting a list of all questions information
    questionsNum = 0 
    score = 0
    quiz = []
    run = True
    while run:
        if len(questions) != 0: # checking if we have questions left
            index = randint(0, len(questions) - 1) # getting a random index from questions list
            question = questions[index]
            print('_'*50+"\n")
            print(f"Q{questionsNum + 1}- {question.getBody()}") 
            
            choices = question.getChoices() 
            for i in range(1, 5):
                print(f"{i}. {choices[i - 1]}")
            answer = getValidInput()
            if answer != 'Q':
                # giving the choice body to isCorrect method(the answer is between 1 and 4 so we need to subtract 1 to get the index)
                if question.isCorrect(choices[int(answer) - 1]): 
                    print('\nCORRECT!')
                    score += 1
                else:
                    print('\nWRONG!')

                questionsNum += 1
                # this dictionary will be added to quiz list which will be the input for writeAnswers function
                answeredQuestion = {'question': question, 'userAnswer': choices[int(answer) - 1], 'questionNum' : questionsNum }
                quiz.append(answeredQuestion)
                # removing the question from questions list so we don't get it twice
                questions.remove(question)
                print('The right answer is:', question.getAnswer())
            else:
                # ending the loop if the user entered q
                run = False
        else:
            # ending the loop if we run out of questions
            run = False
            
    finalScore = getScore(score, questionsNum)

    print(f"\n\nYour final score is: %.2f" % finalScore + '%')
    writeAnswers(quiz) 

    
main()   