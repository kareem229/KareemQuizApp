import unittest
from project import Question, QuizBrain

class TestQuizApp(unittest.TestCase):
    def test_question_initialization(self):
        question_text = "What is the capital of France?"
        correct_answer = "Paris"
        choices = ["London", "Berlin", "Madrid", "Paris"]
        question = Question(question_text, correct_answer, choices)

        self.assertEqual(question.question_text, question_text)
        self.assertEqual(question.correct_answer, correct_answer)
        self.assertEqual(question.choices, choices)

    def test_quizbrain_initialization(self):
        question1 = Question("Question 1", "Answer 1", ["Option 1", "Option 2", "Option 3", "Answer 1"])
        question2 = Question("Question 2", "Answer 2", ["Option 1", "Option 2", "Option 3", "Answer 2"])
        questions = [question1, question2]

        quiz_brain = QuizBrain(questions)

        self.assertEqual(quiz_brain.question_no, 0)
        self.assertEqual(quiz_brain.score, 0)
        self.assertEqual(quiz_brain.questions, questions)
        self.assertIsNone(quiz_brain.current_question)

    def test_has_more_questions(self):
        question1 = Question("Question 1", "Answer 1", ["Option 1", "Option 2", "Option 3", "Answer 1"])
        question2 = Question("Question 2", "Answer 2", ["Option 1", "Option 2", "Option 3", "Answer 2"])
        questions = [question1, question2]

        quiz_brain = QuizBrain(questions)

        self.assertTrue(quiz_brain.has_more_questions())
        quiz_brain.question_no = len(questions)
        self.assertFalse(quiz_brain.has_more_questions())

    def test_next_question(self):
        question1 = Question("Question 1", "Answer 1", ["Option 1", "Option 2", "Option 3", "Answer 1"])
        question2 = Question("Question 2", "Answer 2", ["Option 1", "Option 2", "Option 3", "Answer 2"])
        questions = [question1, question2]

        quiz_brain = QuizBrain(questions)

        self.assertEqual(quiz_brain.next_question(), "Q.1: Question 1")
        self.assertEqual(quiz_brain.next_question(), "Q.2: Question 2")


    def test_get_score(self):
        question1 = Question("Question 1", "Answer 1", ["Option 1", "Option 2", "Option 3", "Answer 1"])
        question2 = Question("Question 2", "Answer 2", ["Option 1", "Option 2", "Option 3", "Answer 2"])
        questions = [question1, question2]

        quiz_brain = QuizBrain(questions)
        quiz_brain.score = 1
        quiz_brain.question_no = 2

        self.assertEqual(quiz_brain.get_score(), (1, 1, 50))

if __name__ == "__main__":
    unittest.main()
