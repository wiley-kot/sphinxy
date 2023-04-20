from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    """
    A riddle and the answer

    question (str): The question for the riddle
    answer (str): The answer for the riddle
    """
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """
        Checks an answer against the riddle

        Args:
            answer: The answer provided

        Returns:
            bool: Whether the answer was correct or wrong
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """
        Returns a hint of the answer (partial string of the answer). Progressive calls get the next
        character in the answer

        Returns:
            str: a single character from the answer.
        """
        yield from iter(self.answer)
