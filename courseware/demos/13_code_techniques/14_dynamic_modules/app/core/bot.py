from abc import ABC, abstractmethod
import logging


class Bot(ABC):
    name: str

    def __init__(self):
        self.logger = logging.getLogger(f"{self.name.lower()}_bot")

    @abstractmethod
    def run(self) -> None:
        """run"""
        pass
