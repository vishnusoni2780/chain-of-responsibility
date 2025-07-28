from attacks.classifier import Classifier
from attacks.Attack1 import Attack1
from attacks.Attack2 import Attack2

class Runner:
    def __init__(self):
        self.classifiers: list[Classifier] = [
            Attack1(),
            Attack2(),
        ]

    def classify(self):
        for classifier in self.classifiers:
            classifier.run()
