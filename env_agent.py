from mesa import Agent
import numpy as np
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Environment class
class Environment:
    def __init__(self):
        self.weather = random.choice(['Clear', 'Rainy', 'Foggy', 'Snowy'])
        self.road_condition = random.choice(['Dry', 'Wet', 'Icy'])
        self.presence_of_pedestrians = random.choice([True, False])
        self.presence_of_animals = random.choice([True, False])
        self.road_type = random.choice(['Straight', 'Curved', 'Banked', 'Turning'])