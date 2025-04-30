from car import Car
from mesa import Agent
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Car class
class AutonoumousCar(Car):
    def __init__(self, config, strictness):
        self.time_trained = min(max(1 - strictness + random.gauss(0, 0.1), 0), 1)
        self.driving_expertise = min(max(max(self.time_trained, 0.5*strictness) + random.gauss(0, 0.1), 0), 1)
        self.reaction_time = min(max(random.gauss(0.2, 0.01), 0), 1)
        self.fatigue = 0
        self.decision_making = min(max(2 * (0.6 * self.driving_expertise * self.time_trained * max(random.gauss(1.1, 0.1), 0)) ** 0.5, 0), 1)
        self.consistency = min(max(1.2 * strictness + random.gauss(0, 0.1), 0), 1)

        super().__init__(
            driving_expertise=self.driving_expertise,
            reaction_time=self.reaction_time,
            fatigue=self.fatigue,
            decision_making=self.decision_making,
            consistency=self.consistency
        )