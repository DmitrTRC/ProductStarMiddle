import json


from dataclasses import dataclass
from typing import List
from typing import Dict


@dataclass
class Question:
    task: str = ''
    answer: List[str] = None


class QuestionGenerator:

    def __init__(self, path: str):
        self.path: str = path
        self._questions: Dict = self._load_quiz_set()
        self.get_next_question = self.question_generator()

    def _load_quiz_set(self) -> Dict:
        return json.load(open(self.path, 'r'))

    def question_generator(self):
        for question, answer in self._questions.items():
            yield Question(question, answer)


class QuizGame:
    data_filename = 'questions.json'

    def __init__(self):
        self._questions = QuestionGenerator(self.data_filename)
        self.current_question: Question = Question()
        self._right_answers = 0
        self._wrong_answers = 0

    def run(self):
        for self.current_question in self._questions.get_next_question:

            is_right = self._check_answer(self._ask_question())

            self._set_score(is_right)
            self._show_result(is_right)

        self._show_score()

    def _ask_question(self) -> str:
        print(self.current_question.task)
        answer: str = self._normalize(input())
        return answer

    def _check_answer(self, answer: str) -> bool:

        # Normalize to lower right answers
        for right_answer in self.current_question.answer:

            if self._normalize(right_answer) == self._normalize(answer):
                return True

        return False

    def _show_result(self, is_right: bool):

        if is_right:
            print('Right!')
        else:
            print(f'Wrong! Write one of this answers: {self.current_question.answer[0]} ')

    def _show_score(self):
        print(f'Right answers: {self._right_answers}')
        print(f'Wrong answers: {self._wrong_answers}')

    @staticmethod
    def _normalize(param: str) -> str:
        return param.lower().strip()

    def _set_score(self, is_right: bool):
        if is_right:
            self._right_answers += 1
        else:
            self._wrong_answers += 1


if __name__ == '__main__':
    quiz_game = QuizGame()
    quiz_game.run()

    print('Bye!')
