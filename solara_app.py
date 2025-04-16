# import solara
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# from io import BytesIO
# import base64

# # Use your existing simulation logic
# from model import run_simulations

# @solara.component
# def CrashSimulationDashboard():
#     num_runs = solara.reactive(500)
#     df = solara.reactive(pd.DataFrame())

#     def run_simulation():
#         df.value = run_simulations(num_runs.value)
#         df.value.to_csv("solara_simulation_results.csv", index=False)  

#         # Save heatmap image
#         car_attributes = ['Driving_Expertise', 'Reaction_Time', 'Fatigue', 'Decision_Making', 'Consistency']
#         correlation_df = df.value[car_attributes + ['Crash_Probability', 'Crash_Severity']]
#         corr = correlation_df.corr()

#         plt.figure(figsize=(8, 6))
#         sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
#         plt.title('Correlation between Car Attributes and Crash Outcomes')
#         plt.tight_layout()
#         plt.savefig("solara_correlation_heatmap.png")  
#         plt.close()

#     solara.Title("Car Crash Simulation Dashboard")

#     with solara.Column():
#         solara.SliderInt("Number of simulations", value=num_runs, min=100, max=5000, step=100)
#         solara.Button("Run Simulation", on_click=run_simulation)

#         if not df.value.empty:
#             solara.Markdown(f"**{len(df.value)} simulations completed.**")
#             solara.Markdown(f"Results saved to `solara_simulation_results.csv`")
#             solara.Markdown(f"Heatmap saved to `solara_correlation_heatmap.png`")

#             solara.DataFrame(df.value.head(20))

#             car_attributes = ['Driving_Expertise', 'Reaction_Time', 'Fatigue', 'Decision_Making', 'Consistency']
#             correlation_df = df.value[car_attributes + ['Crash_Probability', 'Crash_Severity']]
#             corr = correlation_df.corr()

#             fig, ax = plt.subplots(figsize=(8, 6))
#             sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
#             plt.title('Correlation between Car Attributes and Crash Outcomes')
#             plt.tight_layout()

#             buf = BytesIO()
#             plt.savefig(buf, format="png")
#             buf.seek(0)
#             img_base64 = base64.b64encode(buf.read()).decode('utf-8')
#             buf.close()

#             solara.Image(f"data:image/png;base64,{img_base64}")

# @solara.component
# def Page():
#     CrashSimulationDashboard()
import solara
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Use your existing model code directly
from model import Environment, Car

@solara.component
def ControlledCarCrashSimulationDashboard():
    num_runs = solara.reactive(100)

    # Sliders for car attributes
    driving_expertise = solara.reactive(0.75)
    reaction_time = solara.reactive(0.75)
    fatigue = solara.reactive(0.5)
    decision_making = solara.reactive(0.75)
    consistency = solara.reactive(0.75)

    results_df = solara.reactive(pd.DataFrame())

    def run_simulation():
        results = []
        for _ in range(num_runs.value):
            env = Environment()
            car = Car(autonomous=False)
            car.driving_expertise = driving_expertise.value
            car.reaction_time = reaction_time.value
            car.fatigue = fatigue.value
            car.decision_making = decision_making.value
            car.consistency = consistency.value

            prob, severity = car.evaluate_crash_risk(env)
            results.append({
                'Crash_Probability': prob,
                'Crash_Severity': severity
            })

        df = pd.DataFrame(results)
        results_df.value = df
        df.to_csv("controlled_simulation_results.csv", index=False)

        # Save histogram of crash severity
        plt.figure(figsize=(8, 5))
        sns.histplot(df['Crash_Severity'], bins=20, kde=True)
        plt.title("Crash Severity Distribution")
        plt.xlabel("Severity")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig("controlled_crash_severity_histogram.png")
        plt.close()

    solara.Title("Controlled Car Crash Simulation")

    with solara.Column():
        solara.SliderInt("Number of Simulations", value=num_runs, min=50, max=2000, step=50)

        solara.SliderFloat("Driving Expertise", value=driving_expertise, min=0.5, max=1.0, step=0.01)
        solara.SliderFloat("Reaction Time (sec)", value=reaction_time, min=0.2, max=1.5, step=0.01)
        solara.SliderFloat("Fatigue", value=fatigue, min=0.0, max=1.0, step=0.01)
        solara.SliderFloat("Decision Making", value=decision_making, min=0.5, max=1.0, step=0.01)
        solara.SliderFloat("Consistency", value=consistency, min=0.5, max=1.0, step=0.01)

        solara.Button("Run Simulation", on_click=run_simulation)

        if not results_df.value.empty:
            solara.Markdown(f"**{len(results_df.value)} simulations completed.**")
            solara.DataFrame(results_df.value.head(20))

            # Plot crash probability distribution
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.histplot(results_df.value['Crash_Probability'], bins=20, kde=True, ax=ax)
            plt.title("Crash Probability Distribution")
            plt.tight_layout()

            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()

            solara.Image(f"data:image/png;base64,{img_base64}")
            plt.savefig("correlation_heatmap.png")


@solara.component
def Page():
    ControlledCarCrashSimulationDashboard()
