# Why Is the United States So Unhappy Compared to the Happiest Countries?

This project investigates a persistent question:  
**Why is the U.S. consistently less happy than the happiest countries, and can economic indicators help explain this gap?**

As part of my final project for [ME204: Data Engineering for the Social World](https://lse-dsi.github.io/ME204/2025/), I built a data pipeline, from collecting raw global datasets, to designing a relational database, to analyzing reasons behind the gap between the U.S. and the happiest countries of the world. The result is an analysis that's reproducible, and contains both economic data and institutional indicators.

---

## Project Structure
```
project/
├── data/
│ ├── raw/ # Raw API responses (CSV/JSON)
│ └── database.db # SQLite database
├── docs/
│ ├── figures/ # Output plots used in report
│ ├── index_files/ # Created for Quarto Markdown
│ ├── index.html # Ensures the quarto markdown runs
│ └── index.md Public website
├── notebooks/
│ ├── NB01-data-collection.ipynb # API data collection
│ ├── NB02-data-processing.ipynb # Database design & ETL
│ └── NB03-analysis.ipynb  # Exploratory analysis
├── scripts/ # # Utility scripts
└── README.md # For technical reproduction
```
---
## Setup Instructions
### Requirements

- Python 3.8+
- Install these packages (or run in JupyterLab):
```bash
pip install pandas matplotlib seaborn sqlalchemy plotly
```

# How to Reproduce This Project

## 1. NB01: Data Collection
- Pulled **World Happiness Reports (2018–2024)**  
- CSVs pulled from [Kaggle](https://www.kaggle.com/unsdsn/world-happiness) and the [WHR website](https://worldhappiness.report)  
- Queried **World Bank API** (2018–2023)  
  - Selected indicators: GDP, life expectancy, employment, governance, institutional trust, etc.  
- Filtered to 6 countries:  
  - Top 5 happiest in 2024: **Finland, Denmark, Iceland, Sweden, Netherlands**  
  - Plus: **United States**  

**Output saved to:** `data/raw/`

---

## 2. NB02: Data Cleaning & Database Construction

### World Happiness Report Cleaning
- Combined CSVs across all years  
- Renamed columns to match and keep consistent 
- Removed missing values and kept consistent country-year pairs  
- Final output: a cleaned world_bank_data dataframe that is later converted into a dataset, and then into database.db

### World Bank JSON Cleaning
- No API key is needed. Data is collected using the World Bank's public endpoints.
- Converted JSON into dataframe format  
- Converted country codes from the API to country names 
- Rounded floats and formatted GDP as strings with commas  
- Final output: a cleaned happiness_index_data dataframe that is later converted into a dataset, and then into database.db

### SQLite Database
- Built `database.db` with two tables:  
  - `happiness_scores`: rank, score, and variables  
  - `world_bank_indicators`: GDP, health, governance, etc.  
- Both tables were linked by **country** and **year**

**Output saved to:** `data/database.db`

---

## 3. NB03: Analysis
- Merged both tables on **country** and **year**  using an SQL join
- Filtered for only the 6 target countries  
- Analyzed trends in:
  - **Correlations to Happiness** (U.S. underperforms)
  - **Governance and institutional trust vs. Happiness** (stronger relationship)
- Created year-over-year line plots, comparisons, and scatter visuals

**Figures saved to:** `docs/figures/`  
**Narrative used in:** `docs/index.md`

---

## Data Sources
- **World Happiness Reports**  
  [https://worldhappiness.report](https://worldhappiness.report)
- **Kaggle**  
  [https://www.kaggle.com/unsdsn/world-happiness](https://www.kaggle.com/unsdsn/world-happiness)
- **World Bank API**  
  [https://data.worldbank.org](https://data.worldbank.org)  
  - Example indicator codes:  
    - `NY.GDP.MKTP.CD` → GDP  
    - `SP.DYN.LE00.IN` → Life Expectancy

---

## Database Schema

### Table: `happiness_index_data`

| Column                          | Type    |
|----------------------------------|---------|
| Year                            | INTEGER |
| Rank                            | INTEGER |
| Country                         | TEXT    |
| Happiness_Score                 | REAL    |
| Social_support                  | REAL    |
| Freedom_to_make_life_choices   | REAL    |
| Generosity                     | REAL    |
| Perceptions_of_corruption      | REAL    |

### Table: `world_bank_data`

| Column                             | Type    |
|-------------------------------------|---------|
| Country                             | TEXT    |
| Year                                | INTEGER |
| GDP_Current_USD                     | INTEGER |
| Health_Expenditure_percent_GDP      | REAL    |
| Education_Expenditure_percent_GDP   | REAL    |
| Unemployment_Rate_percent           | REAL    |
| Inflation_Annual_percent            | REAL    |
| FDI_Net_Inflows_percent_GDP         | REAL    |
| Population_Total                    | INTEGER |
| Life_Expectancy_Years               | REAL    |
| Govt_Effectiveness                  | REAL    |
| Rule_of_Law                         | REAL    |
| Control_of_Corruption               | REAL    |
| Political_Stability                 | REAL    |
| Voice_and_Accountability            | REAL    |
| GDP_Per_Capita                      | REAL    |


## Key Project Decisions
- Focused on 6 countries to keep analysis targeted and interpretable  
- Aimed to use List Comprehensions and Vectorized loops
- Cleaned across years manually due to inconsistent WHR formats  
- Used **relational schema** instead of single CSVs for long-term scalability  

---

## How to Verify
Run each notebook in order (**NB01 -> NB02 -> NB03**)

Ensure that:
- `database.db` is created  
- Cleaned `.csv` files exist  
- Final plots are saved in `docs/figures/`  
- Results match those in `index.md`

---

## License
This project was completed as part of the **ME204 Summer 2025** course at the **London School of Economics and Political Science (LSE)**.  

---

## Author
**Jayden Patel**  
Northeastern University  
Business Analytics & Data Science  
**ME204 @ LSE, Summer 2025**