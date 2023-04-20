from __future__ import annotations

from sphinxy.riddle import Riddle



class IncorrectAnswer(Exception):
    ...


class Sphinx:
    """
    A Sphinx to pose riddles to all who dare to venture past
    """
    def __init__(self, name: str):
        """
        Summons a new Sphinx object

        Args:
            name: The sphinx's name
        """
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """
        Returns an introduction of the sphinx

        Returns:
            str: An introduction message
        """

        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        """
        Returns a riddle and an optional hint

        Args:
            include_hint (bool, optional): Whether to return a hint with the answer.

        Returns:
            tuple(str, str(optional)): Returns a tuple of riddle and possible hint in the format (riddle, hint|None)

        """
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """
        Evaluates the given answer to the riddle


        Args:
            answer (str): The given answer to the riddle
            return_hint (bool, optional): Controls whether a hint for the riddle should be returned. Defaults to False


        Raises:
            IncorrectAnswer: Exception for incorrect answer


        Returns:
            str: The result of the evaluation of the answer
        """
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")
