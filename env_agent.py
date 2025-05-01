from mesa import Agent
import numpy as np
import random
import json

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the Environment class
class Environment:
    def __init__(self, weather, road_type):
        self.weather = weather
        self.road_type = road_type
        # Load additional conditions from config.json
        with open("config.json", "r") as config_file:
            additional_conditions = json.load(config_file)
        
        # Extract only the required additional factors
        self.road_condition = additional_conditions.get("environment", {}).get("weather", {}).get(self.weather, {}).get("road_condition", "unknown")
        self.visibility = additional_conditions.get("environment", {}).get("weather", {}).get(self.weather, {}).get("visibility", "unknown")
        self.traffic_density = additional_conditions.get("environment", {}).get("road_type", {}).get(self.road_type, {}).get("traffic_density", "low")
        self.presence_of_pedestrians = additional_conditions.get("environment", {}).get("road_type", {}).get(self.road_type, {}).get("pedestrian_presence", False)
        self.presence_of_animals = additional_conditions.get("environment", {}).get("road_type", {}).get(self.road_type, {}).get("animal_presence", False)
        self.presence_of_foreign_objects = additional_conditions.get("environment", {}).get("road_type", {}).get(self.road_type, {}).get("object_presence", False)
        
        # Print all the conditions and their values
        print("Weather:", self.weather)
        print("Road Type:", self.road_type)
        print("Road Condition:", self.road_condition)
        print("Visibility:", self.visibility)
        print("Traffic Density:", self.traffic_density)
        print("Presence of Pedestrians:", self.presence_of_pedestrians)
        print("Presence of Animals:", self.presence_of_animals)
        print("Presence of Foreign Objects:", self.presence_of_foreign_objects)

if __name__ == "__main__":
    # Create an instance of the Environment class
    env = Environment(weather="rainy", road_type="city")

