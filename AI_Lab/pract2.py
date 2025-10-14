from experta import *

class StudentFacts(Fact):
    likes = Field(str, mandatory=True)

class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
   
    for interest in interests:
        interest = interest.strip().capitalize()
        if interest:  # make sure it's not empty
            engine.declare(StudentFacts(likes=interest))
   
    engine.run()

if __name__ == "__main__":
    main()
