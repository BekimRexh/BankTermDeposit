import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import category_encoders as ce


__data_columns = None
__model = None


def engineer_features(features):
    def data_process(df, remove_rows):

        # check types of jobs and count, need to account for the unknowns somehow, for now drop?
        df['job'].value_counts()
        mask = (df['job'] == 'unknown')
        if remove_rows:
            df = df[~mask]
        else:
            df.loc[mask, 'job'] = None

        df2 = df.copy() 

        # education check, unknowns present, maybe can infer job through education level later on?
        def education_level(x):
            if str(x) == 'primary':
                return 1
            elif str(x) == 'secondary':
                return 2
            elif str(x) == 'tertiary':
                return 3
            return 0

        df3 = df2.copy()
        df3['education'] = df2['education'].apply(education_level)

        le = LabelEncoder()
        columns_encode = ['default', 'housing', 'loan']

        for col in columns_encode:
            df3[col] = le.fit_transform(df3[col])

        df4 = df3.copy()

        # student, can't be primary as a student
        mask = ((df3['job'] == 'student') & (df4['education'].dropna().astype(int) <= 1))
        if remove_rows:
            df4 = df4[~mask]
        else:
            df4.loc[mask, 'education'] = None

        # can't be retired and below 40 like what?
        mask = (df4["job"] == "retired") & (df4["age"] < 60)
        if remove_rows:
            df4 = df4[~mask]
        else:
            df4.loc[mask, "job"] = None

        # I mean if you are over 70 you are not doing labor or housemaid jobs anymore
        mask = (df4['age'] > 80) & (~df4['job'].isin(['retired']))
        if remove_rows:
            df4 = df4[~mask]
        else:
            df4.loc[mask, "job"] = 'Retired'

        # # older than 40, questionale student i think
        mask = (df4['age'] > 30) & (df4['job'].isin(['student']))
        if remove_rows:
            df4 = df4[~mask]
        else:
            df4.loc[mask, 'job'] = None

        # balance 0 or negative but signed up??? how
        if remove_rows:
            mask = ((df4['balance'] <= 0) & (df['y']==1))
            df4 = df4[~mask]

        
        job_income_dict = {
            'admin.': 2,
            'blue-collar': 1,
            'entrepreneur': 2,
            'housemaid': 1,
            'management': 3,
            'retired': 3,
            'self-employed': 3,
            'services': 1,
            'student': 1,
            'technician': 3,
            'unemployed': 1
        }

        df4['income_level'] = df4['job'].map(job_income_dict)

        # 2 is married
        df4['is_married'] = df4['marital'] == 'married'

        # 3 highly educated
        df4['is_highly_educated'] = df4['education'] == 3

        # 4 average salar is normal for age an occupation, if not then remove?
        AGE_BINS = [17, 28, 40, 50, 70, 100]

        df4['ageBin'] = pd.cut(
            df['age'],
            bins=AGE_BINS,
            labels=['Young Adult', 'Adult', 'Older Adult', 'Senior', 'OAP'],
            right=True
        ).astype(str)

        # 5 contacted before?
        df4['never_contacted_before'] = df4['pdays'] == -1

        #combine some features
        df4['married_young_adult'] = (df4['is_married']==True) & (df4['ageBin']=='Young Adult')
        df4['single_adult_lowbalance'] = (df4['is_married']==False) & (df4['ageBin'].isin(['Young Adult', 'Adult'])) & (df4['balance'] < df4['balance'].mean())

        df4['successb4_Adult_nohouse_married'] = (df4['is_married']==True) & (df4['ageBin'].isin(['Adult'])) & (df4['housing'] == 0) & (df['poutcome']=='success')

        def remove_balance_outliers(df):
            df_out = pd.DataFrame()
            for key, subdf in df4.groupby(['ageBin', 'job']):
                m = np.mean(subdf.balance)
                std = np.std(subdf.balance)
                reduced_df = subdf[(subdf.balance > (m-(std*2))) & (subdf.balance <= (m+(std*2)))]
                df_out = pd.concat([df_out, reduced_df], ignore_index=True)
            
            return df_out

        if remove_rows:
            df5 = df4.copy()
            return remove_balance_outliers(df5)
        else: 
            return df4
    
    features_processed = data_process(features, remove_rows=False)
    
    return features_processed
    


