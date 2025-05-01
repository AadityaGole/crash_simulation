from car import Car
from mesa import Agent
import random
import numpy as np
import math

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Car class
class HumanCar(Car):
    def __init__(self, config, strictness):
        self.time_trained = random.gauss(0.5, 0.1)

        self.driving_expertise = min(max(0.5 * math.tanh(2 * self.time_trained), 0.8 * strictness) + random.gauss(0, 0.04), 1)
        self.fatigue = min(max(random.gauss(0.3, 0.1), 0), 1)
        self.reaction_time = max(((1 + math.tanh(5 * self.fatigue))) * (1 - 0.2 * self.driving_expertise) / 2 + random.gauss(0, 0.04), 0.3)
        self.decision_making = min(max(((1 - math.tanh(10 * self.fatigue))) * (self.time_trained) / 2 + random.gauss(0, 0.04), 0), 1)
        self.consistency = min(max(0.5 + (self.time_trained * self.driving_expertise) / 2 + random.gauss(0, 0.1), 0), 1)

        super().__init__(
            driving_expertise=self.driving_expertise,
            reaction_time=self.reaction_time,
            fatigue=self.fatigue,
            decision_making=self.decision_making,
            consistency=self.consistency
        )