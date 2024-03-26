class Human:
    def __init__(self, name) -> None:
        self.name = name

    def answer_question(self, question):
        print('Really interesting question! I dont know')

class Student(Human):
    def ask_question(self, someone, question):
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()

class Curator(Human):
    def answer_question(self, question):
        if question == "I'm sad, what to do?":
            print('Keep calm, everything will be OK. Do you want some kitty clips?')
        else:
            super().answer_question(question)

class Mentor(Human):
    def answer_question(self, question):
        if question == "When the holidays?":
            print('Ask your teammates!')  
        else:
            super().answer_question(question)

class CodeReviewer(Human):
    def answer_question(self, question):
        if question == "What's wrong with my project?":
            print('Oh, question about the project, I love that.') 
        else:
            super().answer_question(question)            

vova = Student('Vova')
sam = Mentor('Sam')
masha = CodeReviewer('Masha')
maya = Curator('Maya')

question = 'When the holidays?'
vova.ask_question(sam, question)
vova.ask_question(masha, question)
vova.ask_question(maya, question)

question = "What's wrong with my project?"
vova.ask_question(sam, question)
vova.ask_question(masha, question)
vova.ask_question(maya, question)

question = "I'm sad, what to do?"
vova.ask_question(sam, question)
vova.ask_question(masha, question)
vova.ask_question(maya, question)