from abc import ABC, abstractmethod


class Classifier(ABC):
    @abstractmethod
    def run(self):
        pass
