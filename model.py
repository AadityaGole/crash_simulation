import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from car_agent import Car
from env_agent import Environment

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Run multiple simulations
def run_simulations(num_runs=100):
    results = []

    for _ in range(num_runs):
        env = Environment()
        car = Car(autonomous=random.choice([True, False]))
        prob, severity = car.evaluate_crash_risk(env)

        results.append({
            'Autonomous': car.autonomous,
            'Driving_Expertise': car.driving_expertise,
            'Reaction_Time': car.reaction_time,
            'Fatigue': car.fatigue,
            'Decision_Making': car.decision_making,
            'Consistency': car.consistency,
            'Weather': env.weather,
            'Road_Condition': env.road_condition,
            'Pedestrians': env.presence_of_pedestrians,
            'Animals': env.presence_of_animals,
            'Road_Type': env.road_type,
            'Crash_Probability': prob,
            'Crash_Severity': severity
        })

    return pd.DataFrame(results)

if __name__ == "__main__":
    df = run_simulations(1000)
    df.to_csv("simulation_results.csv", index=False)

    print(df.describe())
    print(df.head())

    # Correlation matrix
    car_attributes = ['Driving_Expertise', 'Reaction_Time', 'Fatigue', 'Decision_Making', 'Consistency']
    correlation_df = df[car_attributes + ['Crash_Probability', 'Crash_Severity']]
    corr = correlation_df.corr()

    # Heatmap plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation between Car Attributes and Crash Outcomes')
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()
