import simple_chalk

class CovidExpert:
    def __init__(self):
        self.questions = []
        self.score = []

    def SetData(self, questions):
        self.questions = questions
    
    def findScore(self):
        if(self.questions == []): return
        print("\n\n------------Expert System-----------\n")
        for i in range(0,len(self.questions), 1):
            print((simple_chalk.blue.bold("Question : ")+self.questions[i]["que"]))
            print(simple_chalk.blue.bold("User     : "),end='')
            score = (input())
            print()
            if(score.lower() == "yes" or score.lower() == "y"):
                self.score.append(self.questions[i]["weight"])
            else:
                self.score.append(0)

    def checkOutcome(self):
        if(self.score == []): return
        score = sum(self.score)
        totalScore = 0
        for i in range(0, len(self.questions),1):
            totalScore = totalScore + self.questions[i]["weight"]
        percantage = (score/(totalScore))*100
        return percantage

   

    





expSys = CovidExpert()
questionList = [
    {
        "que" : "Do you have fever? (Y/N)",
        "weight" : 1
    },
    {
        "que" : "Do you have cough? (Y/N)",
        "weight" : 1
    },
    {
        "que" : "Do you have tiredness? (Y/N)",
        "weight" : 1
    },
    {
        "que" : "red or irritated eyes? (Y/N)",
        "weight" : 1.5
    },
    {
        "que" : "Do you have loss of taste or smell? (Y/N)",
        "weight" : 2
    },
    {
        "que" : "Do you have difficulty breathing or shortness of breath? (Y/N)",
        "weight" : 2
    },
    {
        "que" : "Do you have loss of speech or mobility, or confusion? (Y/N)",
        "weight" : 3
    },
    {
        "que" :  "Do you have chest pain? (Y/N)",
        "weight" : 3
    } 
]

expSys.SetData(questionList)
expSys.findScore()
outcome = expSys.checkOutcome()

print(simple_chalk.magenta.bold("You have "+ str(outcome)+ "% probability of COVID\n\n"))

if(outcome>65):
    print(simple_chalk.red.bold("Diagnosis   : There are high chances that you are covid positive. \n              Please take consultation from doctor "))
    print(simple_chalk.red.bold("Precautions : Isolate Yourself, Get RTPCR test done"))
else:
    print(simple_chalk.green.bold("Diagnosis   : No symtoms of COVID. You are healthy. Stay home stay safe"))

print("\n\n\n")