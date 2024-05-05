import pandas as pd
all= pd.read_csv('C:\\Users\\zaara\\Downloads\\data.csv',usecols=['Duration','Pulse','Maxpulse','Calories'])

underdt= all.loc[all['Duration']>60]
mp=all.loc[all['Maxpulse']>150]
cl=all.loc[all['Calories']>400]

a=input('enter to check performace was over, under or avg: ')

if a=='over':
    over=all.loc[(all['Duration']<60)&(all['Maxpulse']>150)&(all['Calories']>300)]
    print ('indices of those exerting themselves more than neccessary are: ',over.index)
elif a=='under':
    under=all.loc[(all['Duration']<60)&(all['Maxpulse']<120)&(all['Calories']<200)]
    print ("The underperforming indices are: ",under.index)
else:
    avg=all.loc[(all['Duration']<=60)&(all['Maxpulse']<=150)&(all['Calories']<=300)]
    print('Normal performace from the following indices: ',avg.index)
