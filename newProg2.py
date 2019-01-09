def Trivia():
 score=0
 myFile = open("farming2.csv","r") # opens the CSV file and stores it in the array myFile
 players = myFile.readlines() # reads the lines of the CSV file into the variable players
 questionno=1
 while questionno < 4:
    for p in players:
        data = p.split(",") #splits each cell of the CSV file into its parts
        questions = data[0]
        answera = data[1]
        answerb = data[2]
        answerc = data[3]
        CorrectAnswer = data[4]
        print("Question #",questionno)
        print(questions) #prints the question and the 3 answers
        time.sleep(0.5)
        print(answera)
        time.sleep(0.5)
        print(answerb)
        time.sleep(0.5)
        print(answerc)
        time.sleep(0.5)
        answer = input("Answer? ") #asks the user for their answer
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        if answer == CorrectAnswer: #checks if the answer is correct and prints approptiate responses
            print("That is the correct answer")
            score=score+1
            time.sleep(1)
        else:
            print("That is not the correct answer")
            time.sleep(1)
        print("Your current score is", score)
        print("")
        questionno = questionno+1

 myFile.close()
Trivia()
