from random import sample

class Question():
    def __init__(self, body, choices, answer):
        self._body = body
        self._choices = choices
        self._answer = answer
        
    def getChoices(self):
        # This method returns a list of choices in a random order (without modifying the existing choices list).
        return sample(self._choices, len(self._choices))
        
    def isCorrect(self, userAnswer):
        return userAnswer == self._answer
    
    def getBody(self):
        return self._body
    
    def getAnswer(self):
        return self._answer


def readQuestions(fileName):
    # This function reads questions from the questions.txt file and returns a list of Question objects.
    with open(fileName, 'r') as file:
        lines = file.read().splitlines()

    questions = []
    for i in range(0, len(lines), 6):
        body = lines[i]
        choices = lines[i + 1:i + 5]
        answer = lines[i + 5]
        question = Question(body, choices, answer)
        questions.append(question)

    return questions


def writeAnswers(quiz):
    # This function writes the questions, user answers, and correct answers to the answers.txt file.
    with open('answers.txt', 'w') as file:
        for question in quiz:
            body = question['question'].getBody()
            userAnswer = question['userAnswer']
            correctAnswer = question['question'].getAnswer()
            questionNum = question['questionNum']
            
            file.write(f"Question #{questionNum}: {body}\n")
            file.write(f"Your Answer: {userAnswer}\n")
            file.write(f"Correct Answer: {correctAnswer}\n\n")


def getValidInput():
    # This function validates and returns the user's input.
    while True:
        answer = input("Enter your choice (number) or 'Q' to quit: ")
        if answer.isdigit() and 1 <= int(answer) <= 4:
            return answer
        elif answer.upper() == 'Q':
            return answer.upper()
        print('\nInvalid input. Please try again.')


def getScore(score, questionsNum):
    # This function calculates and returns the user's score.
    if questionsNum != 0:
        return (score / questionsNum) * 100
    else:
        return 0.0


def main():
    questions = readQuestions('questions.txt')
    questionsNum = 0
    score = 0
    quiz = []
    run = True
    
    while run and questions:
        question = sample(questions, 1)[0]
        questions.remove(question)
        
        print('_' * 50 + "\n")
        print(f"Q{questionsNum + 1}- {question.getBody()}")

        choices = question.getChoices()
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
            
        answer = getValidInput()
        
        if answer == 'Q':
            run = False
        else:
            userAnswer = choices[int(answer) - 1]
            if question.isCorrect(userAnswer):
                print('\nCORRECT!')
                score += 1
            else:
                print('\nWRONG!')

            questionsNum += 1
            answeredQuestion = {'question': question, 'userAnswer': userAnswer, 'questionNum': questionsNum}
            quiz.append(answeredQuestion)
            print('The right answer is:', question.getAnswer())

    finalScore = getScore(score, questionsNum)
    print(f"\nYour final score is: {finalScore:.2f}%")
    writeAnswers(quiz)


if __name__ == "__main__":
    main()
