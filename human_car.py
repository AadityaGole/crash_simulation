from car import Car
from mesa import Agent
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Car class
class AutonoumousCar(Car):
    def __init__(self, config=None):
        self.driving_expertise = min(max(random.gauss(0.8, 0.1), 0), 1)
        self.reaction_time = min(max(random.gauss(0.5, 0.1), 0), 1)
        self.fatigue = min(max(random.gauss(0.2, 0.1), 0), 1)
        self.decision_making = min(max(random.gauss(0.7, 0.1), 0), 1)
        self.consistency = min(max(random.gauss(0.6, 0.1), 0), 1)

        super().__init__(
            driving_expertise=self.driving_expertise,
            reaction_time=self.reaction_time,
            fatigue=self.fatigue,
            decision_making=self.decision_making,
            consistency=self.consistency
        )