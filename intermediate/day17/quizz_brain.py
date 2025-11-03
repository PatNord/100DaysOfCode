class QuizzBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            player_input = input(f"Q{self.question_number}: {question.text} True/False? >").strip().lower()
            if player_input not in {"true", "false"}:
                print("Invalid choice. Type True or False.")
                continue
            else:
                if player_input == "true" and question.answer == True or player_input == "false" and question.answer == False:
                     return True
                else:
                     print("Wrong answer!")
                     return False
    
    def still_has_questions(self):
            if self.question_number > len(self.question_list):
                print("You won the game!")
                return False
            else:
                 return True
                
