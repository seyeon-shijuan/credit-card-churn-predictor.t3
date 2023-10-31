import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_DIR = "../../data/"

df = pd.read_csv(DATA_DIR+"BankChurners.csv").iloc[:, 1:-2]
df_original = df.copy()

'''다중공선성 제거'''
# Credit_Limit 과 Avg_Open_To_Buy는 강한 상관관계가 있으므로 open to buy 열 삭제
df = df.drop(['Avg_Open_To_Buy'], axis=1)

df['Attrition_Flag'] = df['Attrition_Flag'].apply(lambda x: 0 if x == 'Existing Customer' else 1)

'''Label Encoding'''
gender = {'M': 0, 'F': 1}
df['Gender']=df['Gender'].map(gender)

marital_status = {'Married': 1,'Single': 2, 'Divorced': 3}
df['Marital_Status'] = df['Marital_Status'].map(marital_status)

education_level = {'Uneducated': 1,'High School': 2, 'Graduate': 3, 'College': 4, 'Post-Graduate': 5, 'Doctorate': 6}
df['Education_Level'] = df['Education_Level'].map(education_level)

income_cat = {'Less than $40K': 1,'$40K - $60K': 2, '$60K - $80K': 3, '$80K - $120K': 4, '$120K +': 5}
df['Income_Category'] = df['Income_Category'].map(income_cat)

card_cat = {'Blue': 1, 'Silver': 2, 'Gold': 3, 'Platinum': 4}
df['Card_Category'] = df['Card_Category'].map(card_cat)

df = df.replace({'Unknown': None})

'''결측치 대체'''
# imputing instance
imputer = KNNImputer(n_neighbors=7)
cols_to_impute = ['Marital_Status', 'Education_Level', 'Income_Category']

# Split the data and fit
X = df.drop(['Attrition_Flag'], axis=1)
y = df['Attrition_Flag']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
X_train[cols_to_impute]=imputer.fit_transform(X_train[cols_to_impute])

X_test[cols_to_impute]=imputer.transform(X_test[cols_to_impute])

train_tot = pd.concat([X_train, y_train], axis=1)
test_tot = pd.concat([X_test, y_test], axis=1)
train_tot.sort_index(ascending=True, inplace=True)
test_tot.sort_index(ascending=True, inplace=True)

df2 = pd.concat([train_tot, test_tot], axis=0)
df2.sort_index(ascending=True, inplace=True)

# KNN 예측값 실수를 반올림하여 정수화
for col in cols_to_impute:
    df2[col] = np.round(df2[col]).astype('int')


# 대소 구분 불가능한 categorycal 변수만 one-hot encoding
to_one_hot = ['Gender', 'Marital_Status']
df3=pd.get_dummies(df2, columns=to_one_hot, drop_first=False)
# column 이름 재설정 후 one-hot encoding 이전 컬럼 제거
new_col_names = {
    'Gender_0': 'Gender_Male',
    'Marital_Status_1': 'Marital_Status_Uneducated',
    'Marital_Status_2': 'Marital_Status_Single',
    'Marital_Status_3': 'Marital_Status_Divorced'
}
df3 = df3.rename(columns=new_col_names)
df3.drop(columns='Gender_1', axis=1, inplace=True)

'''label(y) Attrition_Flag 맨 오른쪽으로 위치 변경'''
new_col_order = [col for col in df3.columns if col != 'Attrition_Flag'] + ['Attrition_Flag']
df3 = df3[new_col_order]

'''standardization'''
scaler = StandardScaler()
scaler.fit_transform(df3.drop('Attrition_Flag', axis=1))
scaled_features = scaler.transform(df3.drop('Attrition_Flag', axis=1))

scaled_features = pd.DataFrame(scaled_features, columns=df3.columns[:-1])
df_final = pd.concat([scaled_features, df3.iloc[:, -1]], axis=1)

'''데이터 저장 및 복원'''
# dataset export (피클로 파이썬 pandas dataframe 객체 그대로 저장)
df3.to_pickle(DATA_DIR + 'base_dataset_before_std.pkl')
df_final.to_pickle(DATA_DIR + 'base_dataset_standardized.pkl')

# 피클 파일에서 pandas dataframe 객체 복원
test = pd.read_pickle(DATA_DIR + 'base_dataset_standardized.pkl') #불러오기

print(test)

