<div align=center style="margin-bottom:30px">
  <img src="data/mdfile/logo.png" width="100px">
</div>

## 신용카드 이탈 고객 예측 모델 및 타겟 마케팅 대응 전략

카드사의 이탈고객과 유지고객을 예측하는 머신러닝 모델 및 데이터 분석을 통해 이탈 위험 고객을 점진적으로 충성 고객으로 만들기 위함<br>
신용카드 고객 데이터를 활용해 이탈고객 예측 모델을 제작하고, 고객 세그먼트 클러스터링하여 타겟 마케팅 및 리텐션 전략 제시

<br>

## 📌 프로젝트 정보
- 새싹 청년취업사관학교 용산2기 핀테크 특화 AI 엔지니어 양성과정
- 1차 데이터 분석 프로젝트
- 기간: 2023.10.30 ~ 2023.11.03
- 주제: 신용카드 이탈 고객 예측 모델 및 타겟 마케팅 대응 전략
- 팀명: 3조
- PPT: [신용카드 이탈 고객 데이터 분석 상세 프레젠테이션 파일 (링크)](https://drive.google.com/file/d/1_HUa9kMu3dpw3HFr71u82RSS6Z9K7CC1/view?usp=sharing)

<br>


## 👑 프로젝트 내용

#### 1. 데이터 EDA 및 전처리

**데이터셋** https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

**데이터셋 정보**

|remark|number|
|:-:|:-:|
|Number of variables|20|
|Number of observations|10127|
|Missing cells|0|
|Duplicate rows|0|

**변수 분석**

- 종속 변인 (dependent variables, y) 
  - Attrition_Flag (1)
- 범주형 변수 (categorical variables)
  - Gender, Education_Level, Marital_Status, Income_Category, Card_Category (5)
- 수치형 변수 (continuous variables)
  - Customer_Age, Dependent_count, Months_on_book, Total_Relationship_Count, Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit, Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio (14)

<br>

**이탈 고객 분석**

![](https://private-user-images.githubusercontent.com/66824510/301483369-8b18652f-67ae-4b23-977f-f935561daf2e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxMTYsIm5iZiI6MTcwNjc4NTgxNiwicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODMzNjktOGIxODY1MmYtNjdhZS00YjIzLTk3N2YtZjkzNTU2MWRhZjJlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTAxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE2NWY2M2JmNzEyNjQxNTQ2YmVkNzRhODZiOWUwYWFkNTEzNGQwZTg1ZjRiN2NkMmM4NGQ1Y2ZjNjMwMjcxOTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.yKJELMjaTgO7VIXBTam7qxtsubFLgQFT2qikj7480-w)

- 데이터셋의 고객풀중에서 가장 큰 portion이 수입 40K 미만 고객(35%) 
- → 따라서 수입과 고객 등급 비례 여부 및 고객 이탈 관계 분석
- **수입과 고객 등급은 일정 수준 이상 비례**하며, **수입 40K미만의 Blue고객의 이탈이 매출손실에 가장 큰 영향**을 줌
- 이탈 고객의 카드거래 건수 도수분포표 분석 결과 최빈구간은 월에 3-4건 결제로 
- **주사용카드가 아니기 때문에 스팟성 결제 후 이탈한 것**으로 분석됨

<br>

**데이터 전처리**

![](https://private-user-images.githubusercontent.com/66824510/301483429-5ca62c1f-93e3-484a-89db-21e977c9f92d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxMjcsIm5iZiI6MTcwNjc4NTgyNywicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODM0MjktNWNhNjJjMWYtOTNlMy00ODRhLTg5ZGItMjFlOTc3YzlmOTJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTAyN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWUzMWQwYzFhYzEzNGIyNTc3M2JlOTI4N2IwZDg5NjVhYTVhN2JlMTJlYWI1MmFiMjgzZGZjZmU4M2MwNGEzNmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.0_YHPArng-gHTU_CBdX1jkNGFukI5Z3jucZOBro6Z6Q)

- **수치형 변수 공선성 제거**
- **범주형 변수 인코딩**: 명목변수(nominal)는 원핫 인코딩, 서열 변수(ordinal)는 라벨 인코딩
- **결측치 처리**: KNN 결측치 대체
  - 기본 데이터 레코드 수가 적어 결측치 제거 불리 (10127건)
  - 조사 항목별 미응답 여부가 다르고 (1개라도 미응답: 3046, 모두 미응답: 7)
  - 유지고객과 이탈고객의 미응답자 비율 비슷하여 결측치 대체가 유리할 것으로 판단
- **데이터 정규화**: Min-Max Scaling
  - Pycaret 테스트에서 standardization, min-max, robust 비교 후 min-max가 가장 높은 성능을 보였기 때문


#### 2. AutoML 활용한 머신러닝 모델링

Pycaret, Autogluon 활용해 베이스 모델로 사용할 모델을 탐색
기본데이터 셋 테스트로 성능이 우수한 모델중 ensemble 및 트리모델 계열 5가지를 선정 후 모델 학습
- Light Gradient Boosting Machine, Random Forest Classifier, AdaBoost Classifier, Decision Tree Classifier, Bagging Classifier


![](https://private-user-images.githubusercontent.com/66824510/301483468-695cff72-cf29-4292-a3a2-e5df69c7b037.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxMzYsIm5iZiI6MTcwNjc4NTgzNiwicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODM0NjgtNjk1Y2ZmNzItY2YyOS00MjkyLWEzYTItZTVkZjY5YzdiMDM3LlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTAzNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE4ZjhhMzczNzQ3YmY5YjQ1YjlkMDJhMTkwNTdmM2VhZjk0MThhYjBhNzdhMzBlNGUwZGQ3NTk5YmZkNWYyYjcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.BJdxE4DReVYABTGcDnjFUeKq_L0JDQIi5gdRtXI4CmQ)


- 비즈니스 목표 : 유지 고객이 프로모션 대상으로 분류되어 프로모션 비용 낭비 최소화
- 성능 지표 목표 : 유지 고객의 이탈 예측 고객 비율(FN)을 최소화
- → HIGH RECALL이 되도록 하이퍼파라미터 튜닝 진행
- 최종 선택 모델 LGBM

**Metrics for the test set**

|remark|result|
|:-:|:-:|
|Accuracy|0.9210|
|Precision|0.9399|
|Recall|0.8975|
|F1|0.9182|

<br>

#### 3. 고객 클러스터링

**가설: 모델이 예측한 이탈 확률과 주요 지표를 통해 “유지 고객이지만 이탈 가능성이 높은 고객”을 찾을 수 있을 것이다.**

고객 군집화하여 마케팅 타겟 선정을 위해 <br>
**LGBM 모델의 중요 피처를 활용한 전체 고객 클러스터링**

|feature importance descending|k-means clustering results by silhouette score|
|:-:|:-:|
|![](https://private-user-images.githubusercontent.com/66824510/301483506-8b609c76-2d75-4f43-8dbf-e94161e7ac42.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxNDUsIm5iZiI6MTcwNjc4NTg0NSwicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODM1MDYtOGI2MDljNzYtMmQ3NS00ZjQzLThkYmYtZTk0MTYxZTdhYzQyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTA0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTEzOTA4ZDk4YzM2NDU1M2MwY2M5YzRjM2EzYTAyM2MzMGUxYTg4ZmEyNGMxYzk5MjBiOTgwYjQzYTVlYWUxMWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.eRGBOKZ7IVA0-8dvgNCY1Q82GXFP4aaIzlXTgA9ekcs)|![](https://private-user-images.githubusercontent.com/66824510/301483558-04b0e231-d944-41e3-badb-d76316e27c19.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxNTMsIm5iZiI6MTcwNjc4NTg1MywicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODM1NTgtMDRiMGUyMzEtZDk0NC00MWUzLWJhZGItZDc2MzE2ZTI3YzE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI4ZDg1ZDJhMzZmMmQwNjU4MTgxNzIyM2I0YmY4OWM2Y2QzNTVmYmY0ODc0YzEzY2IyZjU2MTg1MjdhZDFmOTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.kefCMYfEfbGKgog67jOKlq0_O64V9ATEmgTpUGuyxe8)|

- LGBM 모델의 이탈 확률을 클러스터링에 활용
  - LGBM 모델의 y값의 threshold가 되는 Predict Proba를 이탈 확률로 규정
- K-Means Clustering
  - 3차원 군집화
  - Predict Proba (이탈확률)은 고정
  - 명목변수를 제외한 전체 피처를 대상으로 2개씩 선택해 모든 클러스터링 경우의 수 계산
  - 클러스터링 결과는 Silhouette Score기준으로 나열
- 상위 케이스 중 세그먼트 분석 및 타겟마케팅 대상 선정을 위한 클러스터 데이터셋 선정
- 최종 축으로 사용된 3차원 피처는 (1) 이탈확률, (2) 1분기 대비 4분기 거래건수 비율과 (3) 12개월 동안의 총 거래금액

<br>

#### 4. 타겟 마케팅 대응 전략
![](https://private-user-images.githubusercontent.com/66824510/301483592-4294fc75-abc0-4f6b-9953-61fbc847998a.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxNjIsIm5iZiI6MTcwNjc4NTg2MiwicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODM1OTItNDI5NGZjNzUtYWJjMC00ZjZiLTk5NTMtNjFmYmM4NDc5OThhLlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTEwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFiZDZjYzVlYzAzMGI0NWM2OGI4NTkxNWViNmJhNjc0NTVlODU5OWIzNDMxZTU3NTcwN2Q2MmQ5MTkyMTFjZjQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Lact7TEWFYXYyV_b1FrL16kqAMhfqmllRnmoU7fIr5U)

우측 상단 3차원 K-Means Clustring Visualization Chart에서

- 노란 군집: 이탈고객 1587명과 유지 40명 으로 구성되어 이탈 고객군으로 분석
  - 이탈고객의 복귀와 로열티 고객으로의 안착을 위해 이 40명에 먼저 마케팅을 집행하는 전략
  - 앱푸시나, 기프티콘, 마트 페이백을 통해 ‘소액 결제를 유도’하여 1차 리텐션 마케팅을 진행
  - 1차 리텐션 마케팅을 통해 1000 달러로 2만3천 달러의 최대 추정 이익을 달성 가능
- 보라 군집: 좌표평면상 가장 안쪽에 위치한 고객군으로 최상위 고객군으로 분석
  - 대체적으로 전체 유지고개 대비 우량고객이면서도. 계좌수를 매우 적게 가지고 있는 것으로 나타남
  - 기존 유지 고객 대비 신용한도가 평균적으로 66% 높고 총 거래건수는 평균적으로 61% 높음
- 초록 군집: 전체 유지 고객과 유사한 분포를 띄어 일반 고객으로 분석

<br>

![](https://private-user-images.githubusercontent.com/66824510/301483651-a3dba480-6d5b-4811-b9fd-e940d8f24114.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3ODYxNzEsIm5iZiI6MTcwNjc4NTg3MSwicGF0aCI6Ii82NjgyNDUxMC8zMDE0ODM2NTEtYTNkYmE0ODAtNmQ1Yi00ODExLWI5ZmQtZTk0MGQ4ZjI0MTE0LlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjAxVDExMTExMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE2ODhiOTlhN2VlZGNjNWQxZDgxMTdkMDcwOGNjMzYwNDQ5ZjFkZWMyMzVlNTM5OGE0MDFhMzVmMzY5Mzc0NzMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.SA6Vb0HofoB3PbqklD7zjjWtHbDKYWRAhUGOf6y00zE)

LGBM 모델과 중요 지표를 이용해 고객을 그룹화 한 결과

- **유지고객 중 이탈 고객과 유사한 패턴을 보이는 40명의 위험 고객 발굴**
- 이 40명의 노랑고객군을 유지시키는 리텐션 마케팅을 첫번째 시작으로
- 3개월 뒤 이탈 고객 1587명에 동일한 마케팅을 집행하여 복귀 유저로 전환을 시도하여 매출 신장을 추구
- 복귀 고객은, 기존의 유지고객과 더불어 보라색 이상적 고객군으로 이동할 수 있도록 투트랙 관리
- **1000달러를 들여 얻을수 있는 초기 추정이익은 최대 23549 달러이고, 최대 목표 매출은 2,223,918달러로 전망**

<br><br>


## 🍉 기술 스택
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=Python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/Scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Pycaret](https://img.shields.io/badge/Pycaret-00A2FF?style=flat&logo=Python&logoColor=ffffff)
![Github](https://img.shields.io/badge/Github-181717.svg?style=flat&logo=github&logoColor=white)


<br>


## 👶 팀원 소개

<table border="" cellspacing="0" cellpadding="0" max-width="2000px">
    <tr width="100%">
        <td align="center"><a href= "https://github.com/zave7">권영찬</a></td>
        <td align="center"><a href= "https://github.com/statezeropy">김주영</a></td>
        <td align="center"><a href= "https://github.com/seyeon-shijuan">박세연</a></td>
        <td align="center"><a href= "https://github.com/JangMinJung">장민정</a></td>
    </tr>
    <tr width="100%">
        <td align="center">
          <a href= "https://github.com/zave7">
            <img src="https://avatars.githubusercontent.com/u/41621552?v=4" width="120px"/>
          </a>
        </td>
        <td align="center">
          <a href= "https://github.com/KimJuyoung23">
            <img src="https://avatars.githubusercontent.com/u/38585726?v=4" width="120px"/>
          </a>
        </td>
        <td align="center">
          <a href= "https://github.com/seyeon-shijuan">
            <img src="https://avatars.githubusercontent.com/u/66824510?v=4" width="120px"/>
          </a>
        </td>
        <td align="center">
          <a href= "https://github.com/JangMinJung">
            <img src="https://avatars.githubusercontent.com/u/131653557?v=4" width="120px"/>
          </a>
        </td>
    </tr>
    <tr width="100%">
      <td align="center">
        <small>
        데이터 EDA & 분석<br>
        AutoML<br>
        클러스터 고객분석
        </small>
      </td>
      <td align="center">
        <small>
        데이터 수집 및 EDA<br>
        고객 클러스터링<br>
        프로젝트 발표
        </small>
      </td>
      <td align="center">
        <small>
        데이터전처리 & 분석<br>
        AutoML<br>
        마케팅 대응전략
        </small>
      </td>
      <td align="center">
        <small>
        머신러닝 모델링<br>
        하이퍼파라미터 튜닝<br>
        모델 성능비교
        </small>
      </td>
   </tr>
</table>

<br>

<br>

## 💀 스켈레톤
- 개발 순서에 따른 팀원들의 모든 고민과 연습 과정이 기록된 디렉토리
  - source folder 안에는 파일명_이니셜로 파일 생성
- 기본적으로 개발 및 분석의모든 단계를 개인별로 진행
- 개인 작업물을 최종 통합해 최적화 버전 제작
- 데이터는 pickle, csv등을 통해 상위 디렉토리(data)에 저장하여 공유

<br>

```
src/
├── data/                                   # data
│
└── src/                                    # source material
    ├── EDA/                                # 데이터 EDA
    │
    ├── EDA_by_cluster/                     # Kmeans clustering
    │
    └── model/                              # 모델 학습 및 검증
```
