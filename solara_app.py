import solara
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

# Use your existing simulation logic
from model import run_simulations

@solara.component
def CrashSimulationDashboard():
    num_runs = solara.reactive(500)
    df = solara.reactive(pd.DataFrame())

    def run_simulation():
        df.value = run_simulations(num_runs.value)
        df.value.to_csv("solara_simulation_results.csv", index=False)  

        # Save heatmap image
        car_attributes = ['Driving_Expertise', 'Reaction_Time', 'Fatigue', 'Decision_Making', 'Consistency']
        correlation_df = df.value[car_attributes + ['Crash_Probability', 'Crash_Severity']]
        corr = correlation_df.corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation between Car Attributes and Crash Outcomes')
        plt.tight_layout()
        plt.savefig("solara_correlation_heatmap.png")  
        plt.close()

    solara.Title("Car Crash Simulation Dashboard")

    with solara.Column():
        solara.SliderInt("Number of simulations", value=num_runs, min=100, max=5000, step=100)
        solara.Button("Run Simulation", on_click=run_simulation)

        if not df.value.empty:
            solara.Markdown(f"**{len(df.value)} simulations completed.**")
            solara.Markdown(f"Results saved to `solara_simulation_results.csv`")
            solara.Markdown(f"Heatmap saved to `solara_correlation_heatmap.png`")

            solara.DataFrame(df.value.head(20))

            car_attributes = ['Driving_Expertise', 'Reaction_Time', 'Fatigue', 'Decision_Making', 'Consistency']
            correlation_df = df.value[car_attributes + ['Crash_Probability', 'Crash_Severity']]
            corr = correlation_df.corr()

            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
            plt.title('Correlation between Car Attributes and Crash Outcomes')
            plt.tight_layout()

            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()

            solara.Image(f"data:image/png;base64,{img_base64}")

@solara.component
def Page():
    CrashSimulationDashboard()
