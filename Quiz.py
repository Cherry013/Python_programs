

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_bank = []

class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answers(user_ans, current_question.answer)
        print(f"Your current score is : {self.score}/{self.question_number}")
    
    def check_answers(self,user_answer,ans):
        if user_answer.lower() == ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's Wrong.")
        print(f"The correct answer was : {ans}")


class Question:
    def __init__(self,q_text,q_ans) -> None:
        self.text = q_text
        self.answer = q_ans

class Quiz:
    def __int__(self,q_list):
        self.question_number = 0
        self.question_list = q_list




for que in question_data:
    q_text = que["text"]
    q_ans = que["answer"]
    new_question = Question(q_text,q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("\n"*3)

print("You've Completed the Quiz")
print(f"Your Final score is {quiz.score}/{quiz.question_number}")