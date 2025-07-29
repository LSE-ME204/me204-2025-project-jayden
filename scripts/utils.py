
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