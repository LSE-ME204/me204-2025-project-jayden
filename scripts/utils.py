
# All indicators (economic + health + governance)
# These indicators have different names in the World Bank API, so I renamed them in this dictionary
# for readability purposes
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
