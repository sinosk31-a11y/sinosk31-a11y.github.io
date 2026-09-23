import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

BASE = Path("data/processed")
OUT = Path("visualizations")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(BASE / "project01_master_2023_2025.csv")
for c in df.columns:
    if c not in ["country_code", "country"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

def bar(col, title, xlabel, filename):
    d = df[["country", col]].dropna().sort_values(col)
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.barh(d["country"], d[col])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Country")
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=200, bbox_inches="tight")
    plt.close(fig)

def scatter(x, y, xlabel, ylabel, title, filename):
    d = df[["country", x, y]].dropna()
    r = d[x].corr(d[y])
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.scatter(d[x], d[y])
    m, b = np.polyfit(d[x], d[y], 1)
    xs = np.linspace(d[x].min(), d[x].max(), 100)
    ax.plot(xs, m * xs + b)
    for _, row in d.iterrows():
        ax.annotate(row["country"], (row[x], row[y]),
                    xytext=(4, 4), textcoords="offset points", fontsize=7)
    ax.set_title(f"{title}\nPearson r = {r:.3f}")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=200, bbox_inches="tight")
    plt.close(fig)

bar("gdp_pps_2025", "GDP per Capita by EU Country, 2025", "GDP per capita (PPS per inhabitant)", "01_gdp_per_capita.png")
bar("ai_2025", "Enterprise AI Adoption by EU Country, 2025", "Enterprises using AI (%)", "02_ai_adoption.png")
bar("cloud_2025", "Enterprise Cloud Adoption by EU Country, 2025", "Enterprises using cloud services (%)", "03_cloud_adoption.png")
bar("digital_skills_2025", "Digital Skills by EU Country, 2025", "Digital skills (%)", "04_digital_skills.png")
bar("ict_specialists_2025", "ICT Specialists by EU Country, 2025", "ICT specialists (% of employment)", "05_ict_specialists.png")
scatter("gdp_pps_2025", "ai_2025", "GDP per capita (PPS per inhabitant)", "AI adoption (%)", "GDP per Capita vs AI Adoption, 2025", "06_gdp_vs_ai.png")
scatter("gdp_pps_2025", "cloud_2025", "GDP per capita (PPS per inhabitant)", "Cloud adoption (%)", "GDP per Capita vs Cloud Adoption, 2025", "07_gdp_vs_cloud.png")
scatter("gdp_pps_2025", "digital_skills_2025", "GDP per capita (PPS per inhabitant)", "Digital skills (%)", "GDP per Capita vs Digital Skills, 2025", "08_gdp_vs_digital_skills.png")
scatter("gdp_pps_2025", "ict_specialists_2025", "GDP per capita (PPS per inhabitant)", "ICT specialists (% of employment)", "GDP per Capita vs ICT Specialists, 2025", "09_gdp_vs_ict.png")
bar("ai_change_pp", "Change in Enterprise AI Adoption, 2023–2025", "Change (percentage points)", "10_ai_change.png")
bar("cloud_change_pp", "Change in Enterprise Cloud Adoption, 2023–2025", "Change (percentage points)", "11_cloud_change.png")
bar("digital_skills_change_pp", "Change in Digital Skills, 2023–2025", "Change (percentage points)", "12_digital_skills_change.png")
bar("ict_specialists_change_pp", "Change in ICT Specialists, 2023–2025", "Change (percentage points)", "13_ict_change.png")
