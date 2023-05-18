import unittest

import QuizGame


class QuizTestCase(unittest.TestCase):

    def test_QuestionGenerator_Loading(self):
        testgen = QuizGame.QuestionGenerator('questions.json')
        self.assertEqual(testgen._load_quiz_set().__len__(), 12)

    def test_QuestionGenerator_Generator(self):
        testgen = QuizGame.QuestionGenerator('questions.json')
        self.assertEqual(testgen.question_generator().__next__().task, 'What is actual Python version?')

    def test_QuizGame_CheckAnswer(self):
        test_game = QuizGame.QuizGame()
        test_game.current_question = test_game._questions.get_next_question.__next__()
        self.assertTrue(test_game._check_answer('3'))


if __name__ == '__main__':
    unittest.main()
