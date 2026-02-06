# SQL-Powered Compound Screening: Kinase Inhibitor Analysis

> **Note:** While this analysis could be done entirely with Python and Pandas, this project integrates **SQL querying** to simulate a real-world drug discovery workflow, demonstrating both database management and Python analysis skills that go beyond typical CSV-based projects.

---

## Project Overview

This project demonstrates the analysis of kinase inhibitor compounds using a combination of **SQL database querying and Python data analysis**. Bioactivity, molecular weight, and clinical phase data were integrated to identify trends in compound potency and prioritize candidates for further investigation.

Unlike my previous Python/Pandas-only projects, this project simulates a **real-world drug discovery workflow**, where data is stored in relational databases and analyzed systematically with Python, highlighting skills relevant to MSc-level applied biomedicine and drug development research.

---

## Dataset Description

- **Source**: ChEMBL-like kinase inhibitor bioactivity dataset  
- **Format**: CSV (`kinase_activity.csv`)  
- **Columns**:
  - `Molecule ChEMBL ID` — Unique identifier for each compound  
  - `Molecular Weight` — Molecular weight of the compound in Daltons  
  - `Molecule Max Phase` — Highest clinical development phase achieved (0–4)  
  - `Value` — Bioactivity measurement (e.g., IC50 in nM)  

**Note:** Some compounds have missing activity values or unknown clinical phases; these were filtered in analysis.

---

## Analysis Methods

1. **Database Integration**  
   - CSV data was imported into a **SQLite database** to simulate relational data storage.  
   - SQL queries were used to **select relevant columns**, filter missing values, and prepare data for analysis.

2. **Python Data Analysis**  
   - Data was loaded from SQL into a Pandas DataFrame.  
   - Bioactivity trends, molecular weight correlations, and clinical phase distributions were visualized using Matplotlib.  

3. **Visualization and Insights**  
   - All plots were saved in a dedicated `plots/` folder, reflecting **reproducible workflow practices**.

---

## Key Visualizations

1. **Distribution of Compound Bioactivity**  
   - Histogram of bioactivity values (IC50) to identify the overall potency profile.  

2. **Log-Scaled Distribution of Bioactivity**  
   - Logarithmic scale histogram highlighting patterns across orders of magnitude in potency.  

3. **Molecular Weight vs Bioactivity**  
   - Scatter plot to explore correlations between molecular size and compound potency.  

4. **Top 10 Most Potent Compounds**  
   - Horizontal bar chart ranking the strongest kinase inhibitors for prioritization.

---

## Biological / Pharmacological Interpretation

- Compounds with **lower IC50 values** are more potent inhibitors.  
- Trends in molecular weight can hint at **drug-likeness** and pharmacokinetic properties.  
- Bioactivity variation across clinical phases can reveal **how candidate selection changes through development**.  
- Top-performing compounds are candidates for **further preclinical or clinical investigation**.

---

## Relevance to Drug Discovery

- Demonstrates **realistic compound screening workflow** using relational databases and Python analytics.  
- Shows ability to **query, filter, and integrate large datasets**, similar to tasks in pharmaceutical research.  
- Prepares for MSc-level projects in **applied biomedicine**, focusing on **drug discovery and development**.

---



