# 데이터 설명 및 구조 정리

|Feature Name|Description|Type|Value|Note|Missing Value|
|:---:|:---:|:---:|:---:|:---|:---|
|CLIENTNUM|고객번호|<span style="color: blue">int</span>||||
|Atrition_Flag|현재 상태(Target)|<span style="color: red">str</span>|['Existing Customer', 'Attrited Customer']|||
|Customer_Age|고객 연령|<span style="color: blue">int</span>||||
|Gender|성별|<span style="color: red">str</span>|['F', 'M']|||
|Dependent_count|부양가족수|<span style="color: blue">int</span>||||
|Education_Level|교육 수준|<span style="color: red">str</span>|['Graduate', 'High School', 'Unknown', 'Uneducated', 'College', 'Post-Graduate', 'Doctorate']||`Unknown`|
|Marital_Status|결혼 상태|<span style="color: red">str</span>|['Married', 'Single', 'Unknown', 'Divorced']||`Unknown`|
|Income_Category|연간소득액|<span style="color: red">str</span>|['Less than $40K', '$40K - $60K', '$80K - $120K', '$60K - $80K', 'Unknown']||`Unknown`|
|Card_Category|카드 등급|<span style="color: red">str</span>|['Blue', 'Silver', 'Gold', 'Platinum']|||
|Months_on_book|은행 거래 기간|<span style="color: blue">int</span>||||
|Total_Relationship_Count|총 보유 계좌|<span style="color: blue">int</span>||||
|Months_Inactive_12_mon|거래내역 없는 거래월 수|<span style="color: blue">int</span>||||
|Contacts_Count_12_mon|거래내역 있는 거래월 수|<span style="color: blue">int</span>||||
|Credit_Limit|신용 한도|<span style="color: blue">float</span>||||
|Total_Revolving_Bal|신용카드의 리볼빙(지불 미루기)한 금액의 합계|<span style="color: blue">int</span>||||
|Avg_Open_To_Buy|신용한도(금액)를 초과할 때 승인 받을 수 있는 금액|<span style="color: blue">float</span>||||
|Total_Amt_Chng_Q4_Q1|1분기 대비 4분기 카드 거래금액 비율|<span style="color: blue">float</span>||||
|Total_Trans_Amt|12개월 동안의 총 거래금액|<span style="color: blue">int</span>||한화 540만원 가량으로 크지 않다. 신용카드 미사용자의 영향을 많이 받았을 것으로 추정된다.||
|Total_Trans_Ct|12개월 동안의 총 거래건수|<span style="color: blue">int</span>||10건 미만인 건수는 없다.||
|Total_Ct_Chng_Q4_Q1|1분기 대비 4분기 거래건수 비율|<span style="color: blue">float</span>||0은 7건인데 4분기 거래 건수가 없다는 것 같다. (최대 3.7)||
|Avg_Utilization_Ratio|평균 카드 이용률|<span style="color: blue">float</span>||||
