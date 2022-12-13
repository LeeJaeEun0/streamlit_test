import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

st.write(
    '''
    # 탐색적 데이터 분석 (EDA) & Seaborn을 통한 데이터 시각화
    ## 정형 데이터
    |대분류|소분류|예시|
    |:-|:-|:-|
    |수치형 데이터<br>(사칙 연산이 가능한 데이터)|연속형 데이터|키, 몸무게, 수입
    ||이산형 데이터|과일 개수, 책의 페이지 수
    |범주형 데이터<br>(범주로 나누어지는 데이터)|순서형 데이터|학점, 순위(랭킹)|
    ||명목형 데이터|성별, 음식종류, 우편번호|
    # 수치형 데이터 numerical data
    > 사칙 연산이 가능한 데이터 (+, -, *, /)
    '''
)

#df
titanic = sns.load_dataset('titanic')
st.write(titanixc) # 적당히 보여줌
# st.table(titanic) #전체를 보여줌

st.write(titanic.info())