
# All indicators (economic + health + governance)
# These indicators have different names in the World Bank API, so I renamed them in this dictionary
# for readability purposes
# I used the world bank open data catalog https://data.worldbank.org/indicator
indicators = {
    'NY.GDP.MKTP.CD': 'GDP_Current_USD',
    'SH.XPD.CHEX.GD.ZS': 'Health_Expenditure_%_GDP',
    'SE.XPD.TOTL.GD.ZS': 'Education_Expenditure_%_GDP',
    'SL.UEM.TOTL.ZS': 'Unemployment_Rate_%',
    'FP.CPI.TOTL.ZG': 'Inflation_Annual_%',
    'BX.KLT.DINV.WD.GD.ZS': 'FDI_Net_Inflows_%_GDP',
    'SP.POP.TOTL': 'Population_Total',
    'SP.DYN.LE00.IN': 'Life_Expectancy_Years',
    
    # Governance indicators that may help the analysis, and give additional data points
    'GE.EST': 'Govt_Effectiveness',
    'RL.EST': 'Rule_of_Law',
    'CC.EST': 'Control_of_Corruption',
    'PV.EST': 'Political_Stability',
    'VA.EST': 'Voice_and_Accountability'
}



# Defined the mapping of the columns that we need to pull from the World Happiness CSV's
year_column_map = {
    '2018': {
        'Rank': 'Overall rank',
        'Country': 'Country or region',
        'Happiness Score': 'Score',
        'Social support': 'Social support',
        'Freedom to make life choices': 'Freedom to make life choices',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions of corruption',
    },

    '2019': {
        'Rank': 'Overall rank',
        'Country': 'Country or region',
        'Happiness Score': 'Score',
        'Social support': 'Social support',
        'Freedom to make life choices': 'Freedom to make life choices',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions of corruption',
    },
    '2020': {
        'Rank': None,  # no explicit rank column, create from index
        'Country': 'Country name',
        'Happiness Score': 'Ladder score',
        'Social support': 'Social support',
        'Freedom to make life choices': 'Freedom to make life choices',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions of corruption',
    },
    '2021': {
        'Rank': None,  # no explicit rank column, create from index
        'Country': 'Country name',
        'Happiness Score': 'Ladder score',
        'Social support': 'Social support',
        'Freedom to make life choices': 'Freedom to make life choices',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions of corruption',
    },
    '2022': {
        'Rank': 'RANK',
        'Country': 'Country',
        'Happiness Score': 'Happiness score',
        'Social support': 'Explained by: Social support',
        'Freedom to make life choices': 'Explained by: Freedom to make life choices',
        'Generosity': 'Explained by: Generosity',
        'Perceptions of corruption': 'Explained by: Perceptions of corruption',
    },
    '2023': {
        'Rank': None,  # no explicit rank column, create from index
        'Country': 'Country name',
        'Happiness Score': 'Ladder score',
        'Social support': 'Social support',
        'Freedom to make life choices': 'Freedom to make life choices',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions of corruption',
    }
}


import sqlite3
import pandas as pd

def load_joined_world_bank_happiness(db_path):
    
    # Loads and joins World Bank and Happiness datasets from a SQLite database.

    # - Connected to the SQLite database containing both datasets
    # - Joined the World Bank and Happiness datasets on Country and Year
    # - Selected all columns from World Bank plus key happiness metrics
    # - Returned the cleaned, merged DataFrame

    # Connected to the SQLite database containing both datasets
    conn = sqlite3.connect(db_path)

    # Joined the World Bank and Happiness datasets on Country and Year
    # Selected all columns from World Bank plus key happiness metrics
    # I inner joined both datasets on the Foreign Key from the world bank data of country and year on the 
    # Primary Key of country and year from the happiness_index_data dataset. This ensured all the matching 
    # I also selected all of the columns from both datasets, so that if I nedded any columns I could use it.
    # I also placed rank before any of the world happiness index data for readability
    query = """
    SELECT 
        h.Rank,
        w.*,
        h.Happiness_Score,
        h.Social_support,
        h.Freedom_to_make_life_choices,
        h.Generosity,
        h.Perceptions_of_corruption
    FROM 
        world_bank_data w
    JOIN 
        happiness_index_data h
    ON 
        w.Country = h.Country AND w.Year = h.Year;
    """

    # Loaded the cleaned dataset that merged World Bank and Happiness data
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df
