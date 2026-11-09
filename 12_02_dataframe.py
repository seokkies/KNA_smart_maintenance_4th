#실습 1
import pandas as pd
df = pd.read_csv("data/12_metro_compressor.csv")
print(df.head())
print(df.tail()) # 0 ~ 199번 확인 , 오일온도 3번 인덱스 NaN


#실습 2
df = pd.read_csv("data/12_metro_digital.csv")
print(df.shape) # (120, 4)
print(df.columns) #Index(['측정시각', '압축기', '타워', '저압스위치'], dtype='str')
print(df['측정시각'].dtype, df['압축기'].dtype, df['타워'].dtype, df['저압스위치'].dtype) #글자 / 숫자 숫자 숫자
print(df.head())

#실습 3
df = pd.read_csv("data/12_metro_compressor.csv")
print(df.info()) # 200행, 오일온도 결측 1건

#실습 4
import numpy as np
df = pd.read_csv("data/12_metro_compressor.csv")
print(df.describe()) 
#          압축압력     배출압력     저장압력     오일온도      모터전류
#mean     9.172200   -0.016950    9.171400   63.181910    2.060850
#50%      9.175000   -0.020000    9.175000   62.900000    0.040000
#모터전류 값이 크게 어긋남
df2 = df[["모터전류", "가동상태"]]
print("가동중일때 모터전류 평균: ", np.round(np.mean(df2["모터전류"][df["가동상태"] == "가동"]), 2))
print("정지중일때 모터전류 평균: ", np.round(np.mean(df2["모터전류"][df["가동상태"] == "정지"]), 2))

#실습 5
import numpy as np
df1 = pd.read_csv("data/12_metro_compressor.csv")
df2 = pd.read_csv("data/12_metro_digital.csv")
print("파일 사이즈:", df1.shape, df2.shape)
print("데이터 타입")
print(df1.dtypes) #compressor는 실수형
print(df2.dtypes) #digital은 정수형
print(df1.info()) # 200행 7열, 오일온도 결측치 하나
print(df2.info()) # 120행 4열, 결측치 없음
print(df1["가동상태"].value_counts()) #정지 104개 / 가동 96개
print(df2["압축기"].value_counts()) # 1 109개 / 0 11개
print(df2["타워"].value_counts()) # 1 112개 / 0 8개
print(df2["저압스위치"].value_counts()) # 0 120개

#실습 6
import pandas as pd
df = pd.read_csv("data/12_metro_small.csv")
print(df.shape) # (30 , 7) 데이터
print(df.info()) # 오일온도 결측치 1개 확인
print(df.describe())
#          압축압력   배출압력    저장압력   오일온도     모터전류
#mean    8.895333  -0.019667   8.896000  54.675862   1.383000
#50%     8.655000  -0.020000   8.660000  55.400000   0.040000
#모터전류의 평균과 중앙값이 크게 차이나는거로 보아, 값의 조건이나 결측이 있을 것으로 예상