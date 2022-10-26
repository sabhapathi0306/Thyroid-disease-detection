import pandas as pd
from sklearn.ensemble import RandomForestClassifier

name= ['age','sex','on thyroxine','query on thyroxine' ,'on antithyroid medication','sick','pregnant','thyroid surgery','I131 treatment','query hypothyroid','query hyperthyroid','lithium','goitre',
'tumor','hypopituitary','psych','TSH measured','TSH','T3 measured','T3','TT4 measured','TT4','T4U measured','T4U','FTI measured','FTI','TBG measured','TBG','referral source','target']
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/thyroid0387.data',sep=',',names = name)



col = ['age','sex','on thyroxine','query on thyroxine' ,'on antithyroid medication','sick,pregnant','thyroid surgery','I131 treatment','query hypothyroid','query hyperthyroid','lithium,goitre',
'tumor','hypopituitary','psych','TSH measured','TSH','T3 measured','T3','TT4 measured','TT4','T4U measured','T4U','FTI measured','FTI','TBG measured','TBG','referral source']
# **DATA_CLEANING**
data.target.dtypes
data['target'] = data['target'].apply(lambda x:x.split('[')[0])
data['age'] = data['age'].apply(lambda x:x if  x >1 and x <100 else '?' )
data = data.drop('referral source',axis = 1)
import numpy as np
for  i in data.columns:
    data[i]  = data[i].replace('?',np.NaN)


sex = {'M':0,'F':1}
ont = {'f':0,'t':1}
data['sex'] = data['sex'].map(sex)
data['on thyroxine'] = data['on thyroxine'].map(ont)
data['query on thyroxine'] = data['query on thyroxine'].map(ont)
data['on antithyroid medication'] = data['on antithyroid medication'].map(ont)
data['sick'] = data['sick'].map(ont)
data['pregnant'] = data['pregnant'].map(ont)
data['thyroid surgery'] = data['thyroid surgery'].map(ont)
data['I131 treatment'] = data['I131 treatment'].map(ont)
data['query hypothyroid'] = data['query hypothyroid'].map(ont)
data['query hyperthyroid'] = data['query hyperthyroid'].map(ont)
data['lithium'] = data['lithium'].map(ont)
data['goitre'] = data['goitre'].map(ont)
data['tumor'] = data['tumor'].map(ont)
data['hypopituitary'] = data['hypopituitary'].map(ont)
data['psych'] = data['psych'].map(ont)
data['TSH measured'] = data['TSH measured'].map(ont)
data['T3 measured'] = data['T3 measured'].map(ont)
data['TT4 measured'] = data['TT4 measured'].map(ont)
data['T4U measured'] = data['T4U measured'].map(ont)
data['FTI measured'] = data['FTI measured'].map(ont)
data['TBG measured'] = data['TBG measured'].map(ont)
data = data.drop(['sick', 'pregnant','I131 treatment', 'query hypothyroid','hypopituitary', 'psych', 'TSH measured', 'T3 measured','TT4 measured','T4U measured',  'FTI measured' ,'query on thyroxine','query hypothyroid','TBG measured','lithium',
       'goitre', 'tumor', 'TBG'],axis = 1)

target = data[['target']]

data = data.drop(['target'],axis = 1).astype('float')

data = data.fillna(data.median())
model = RandomForestClassifier(n_estimators =  250,max_features = 'auto',max_depth= 70,bootstrap = True,n_jobs = -1)
model.fit(data,target)

