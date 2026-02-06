import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)


df = pd.read_csv("kinase_activity.csv", sep=";")
df.head()


conn = sqlite3.connect("drug_screening.db")

df.to_sql(
    name="results",
    con=conn,
    if_exists="replace",
    index=False
)


query = """
SELECT
    [Molecule ChEMBL ID],
    [Molecular Weight],
    [Molecule Max Phase],
    [Value]
FROM results
WHERE [Value] IS NOT NULL;
"""


df_sql = pd.read_sql_query(query, conn)
conn.close()

df_sql.head()



plt.figure()
plt.hist(df_sql["Value"], bins=30)
plt.xlabel("Bioactivity Value (e.g. IC50)")
plt.ylabel("Number of Compounds")
plt.title("Distribution of Compound Bioactivity")
plt.savefig("plots/bioactivity_distribution.png", dpi=300, bbox_inches="tight")
plt.show()




plt.figure()
plt.scatter(df_sql["Molecular Weight"], df_sql["Value"])
plt.xlabel("Molecular Weight (Da)")
plt.ylabel("Bioactivity Value")
plt.title("Molecular Weight vs Bioactivity")
plt.savefig("plots/molecular_weight_vs_bioactivity.png", dpi=300, bbox_inches="tight")
plt.show()




# Remove rows with missing phase or activity
phase_df = df_sql.dropna(subset=["Molecule Max Phase", "Value"])

# Convert phases to int if possible
try:
    phase_df["Molecule Max Phase"] = phase_df["Molecule Max Phase"].astype(int)
except:
    pass  # if conversion fails, leave as is

# Get unique phases
unique_phases = phase_df["Molecule Max Phase"].unique()

# Prepare data for boxplot, only include non-empty arrays
data_to_plot = []
labels = []

for phase in unique_phases:
    values = phase_df[phase_df["Molecule Max Phase"] == phase]["Value"].values
    if len(values) > 0:
        data_to_plot.append(values)
        labels.append(str(phase))

# Only plot if we have at least one dataset
if len(data_to_plot) > 0:
    plt.figure()
    plt.boxplot(data_to_plot, labels=labels)
    plt.xlabel("Clinical Development Phase")
    plt.ylabel("Bioactivity Value")
    plt.title("Bioactivity Across Clinical Development Phases")
    plt.savefig("plots/bioactivity_by_phase.png", dpi=300, bbox_inches="tight")
    plt.show()
else:
    print("No valid phase data to plot!")




top_compounds = df_sql.sort_values("Value").head(10)

plt.figure()
plt.barh(top_compounds["Molecule ChEMBL ID"], top_compounds["Value"])
plt.xlabel("Bioactivity Value")
plt.title("Top 10 Most Potent Compounds")
plt.gca().invert_yaxis()
plt.savefig("plots/top_10_potent_compounds.png", dpi=300, bbox_inches="tight")
plt.show()




plt.figure()
plt.hist(df_sql["Value"], bins=30, log=True)
plt.xlabel("Bioactivity Value (e.g. IC50)")
plt.ylabel("Log Frequency")
plt.title("Log-Scaled Distribution of Compound Bioactivity")
plt.savefig(
    "plots/log_scaled_bioactivity_distribution.png", dpi=300, bbox_inches="tight")
plt.show()
