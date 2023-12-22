# Quiz App

We can devide the functionality of this program into three parts: 
- read questions from the file
- display the questions and take answers from user
- write answered questions to answers file

As for the first part, we need to save the questions from the file in a class so we can easily use them throught the program.
The Question class consist of:
- three instance varialbes:
    - body: get the question body as a string
    - choices:  get the choices as a list of strings
    - answer:  get the answer as a string
- Four methods:
    - getBody:  returns the question body
    - getAnswer:  returns the answer
    - isCorrect:  gets userAnswer as a parametar then compare userAnswer with the correct answer and return True if the answer is correct and false otherwise 
    - getChoices:  return choices in random order

The main function is responsible for calling different functions to display random questions for the user and take input then save the answered questions in answers.txt file. The functions are:
- readQuestions:  reads the questions from questions.txt file and returns a list of Question objects containing all questions.
- getValidInput:  keep asking the user for input until the user enters a number between 1 and 4 or q to quit the program
- getScore: for calculating the user final score 
- writeAnswers:  take a list of dictionaries as an input, each dictionary consist of a question object, the user answer for that question, and the question number. The function write this data to answers.txt file.  
