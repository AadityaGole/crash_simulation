from mesa import Agent
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Car class
class Car:
    def __init__(self, driving_expertise=None, reaction_time=None, fatigue=None,
                 decision_making=None, consistency=None):
        self.driving_expertise = driving_expertise
        self.reaction_time = reaction_time
        self.fatigue = fatigue
        self.decision_making = decision_making
        self.consistency = consistency

    def evaluate_crash_risk(self, environment):
        weather_factor = {'Clear': 0.8, 'Rainy': 1.2, 'Foggy': 1.5, 'Snowy': 1.8}[environment.weather]
        road_factor = {'Dry': 0.8, 'Wet': 1.2, 'Icy': 1.6}[environment.road_condition]
        pedestrian_factor = 1.3 if environment.presence_of_pedestrians else 1.0
        animal_factor = 1.2 if environment.presence_of_animals else 1.0
        road_type_factor = {'Straight': 0.9, 'Curved': 1.2, 'Banked': 1.1, 'Turning': 1.3}[environment.road_type]

        reaction_factor = (1.5 - self.reaction_time) / 1.5
        fatigue_factor = (1.0 - self.fatigue)
        expertise_factor = self.driving_expertise
        decision_factor = self.decision_making
        consistency_factor = self.consistency

        driver_skill = (reaction_factor * fatigue_factor * expertise_factor * decision_factor * consistency_factor)

        base_probability = 0.05
        crash_probability = base_probability * weather_factor * road_factor * pedestrian_factor \
                            * animal_factor * road_type_factor / driver_skill

        crash_probability = min(max(crash_probability, 0.0), 1.0)
        crash_severity = (crash_probability * 10) * (2 - driver_skill)
        crash_severity = min(max(crash_severity, 0.0), 10.0)

        return crash_probability, crash_severity