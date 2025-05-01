from car import Car
from mesa import Agent
import random
import numpy as np
import math

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Car class
class AutonoumousCar(Car):
    def __init__(self, config, strictness):
        self.time_trained = min(max(1 - 0.7 * strictness + random.gauss(0, 0.04), 0), 1)

        self.driving_expertise = min(max(max(0.6 * math.tanh(2 * self.time_trained), 0.8 * strictness) + random.gauss(0, 0.04), 0), 1)
        self.fatigue = 0
        self.reaction_time = min(max(random.gauss(0.2, 0.04), 0), 1)
        self.decision_making = min(max((0.6 * self.driving_expertise * self.time_trained * max(random.gauss(1.1, 0.01), 0)) ** 0.5, 0), 1)
        self.consistency = min(max(0.5 * strictness + math.tanh(self.time_trained * self.driving_expertise) + random.gauss(0, 0.1), 0), 1)

        super().__init__(
            driving_expertise=self.driving_expertise,
            reaction_time=self.reaction_time,
            fatigue=self.fatigue,
            decision_making=self.decision_making,
            consistency=self.consistency
        )