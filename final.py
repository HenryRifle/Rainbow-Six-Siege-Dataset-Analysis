import pandas as pd
import numpy as np
import holoviews as hv
import panel as pn
import warnings
warnings.filterwarnings('ignore')

#first dataframe
df = pd.read_csv("/Users/henrykern/Documents/GitHub/viz-final-project-HenryRifle/datasets/S5_operators.csv", sep=';')


df.drop(['dateid','role','secondaryweapon','secondarygadget','nbdeaths'], axis=1, inplace=True)
operators = df.groupby(['skillrank','primaryweapon', 'operator'], as_index=False)

aggregator = {
    'nbwins': ['sum'],
    'nbkills':['sum'],
    'nbpicks':['sum'],
    
}


operator_sum=operators.agg(aggregator)
operator_sum.columns = ['rank','weapon','operator','wins', 'kills','picks']
operator_sum['win_pct']=100.0*operator_sum.wins/operator_sum.picks
operator_sum = operator_sum.loc[operator_sum['rank'] == ('Gold')]
operator_sum=operator_sum.sort_values(by=["win_pct"],ascending=False)
print(operator_sum)

#second dataframe
df2 = pd.read_csv("/Users/henrykern/Documents/GitHub/viz-final-project-HenryRifle/datasets/S5_objectives.csv", sep=';')
df2.drop(['dateid','gamemode'],axis=1,inplace=True)
objective = df2.groupby(['mapname','objectivelocation','skillrank','role','operator'], as_index=False)

aggregator2 = {
    'nbwins': ['sum'],
    'nbkills':['sum'],
    'nbdeaths':['sum'],
    'nbpicks':['sum'],
}


objective_sum=objective.agg(aggregator2)
objective_sum.columns=['map','site','rank','role','operator','wins','kills','deaths','picks']
objective_sum['win_pct']=100.0*objective_sum.wins/objective_sum.picks
objective_sum = objective_sum.loc[objective_sum['rank'] == ('Gold')]
objective_sum=objective_sum.sort_values(by=["win_pct"],ascending=False)

objective_sum_border=objective_sum.loc[objective_sum['map']==('BORDER')]

objective_sum_border_vent=objective_sum_border.loc[objective_sum_border['site'] == ('TELLERS')]
objective_sum_border_vent.drop(["role",'deaths'],axis=1,inplace=True)
objective_sum_border_vent=objective_sum_border_vent[objective_sum_border_vent.picks > 200]

print(objective_sum_border_vent)

