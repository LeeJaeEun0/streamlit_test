# https://docs.streamlit.io/library/get-started/main-concepts
# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd

# st.write() 마크다운
st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영 합니다.")

# 추첨대상인 13명의 이름을 넣을 수 있는 text_input
# 3 x 4 의 모습으로 입력하기

tabs = st.tabs(['참가자','조']) # 탭을 생성

# 열을 배치하는 메소드 
# st.columns(n): n만큼의 컬럼 리스트를 생성

# 0번째 탭에 컬럼(열)을 넣겠다
columns = tabs[0].columns(4) 

# 화면을 열로 나누어서 배치(열의 위치) - 열 방향대로 tab 되는 이유
# enumerate: index, value 묶음
for idx, col in enumerate(columns): # 인덱스와 객체에 입력
    # col.text_input("조 추첨대상", key=idx)
    for idx2 in range(4): # 4번호출 # 행의 위치
        # key가 겹치면 안 됨
        # col 안에 메소드를 통해서 요소들을 생성해주겠다
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 * 4}", key=f"n{idx+1 + idx2 * 4}")

# 13명이 소속될 조 이름을 넣을 위치
st.write(st.session_state)
# 2번째: 조
columns2 = tabs[1].columns(4) 
for idx, col in enumerate(columns2): # 인덱스와 객체에 입력
    # col.text_input("조 추첨대상", key=idx)
    for idx2 in range(4): # 4번호출 # 행의 위치
        # key가 겹치면 안 됨
        # col 안에 메소드를 통해서 요소들을 생성해주겠다
        col.text_input(f"조 목록 {idx+1 + idx2 * 4}", key=f"g{idx+1 + idx2 * 4}")

## 13명이 소속될 조 이름을 넣을 위치
# st.write(st.session_state)
# np.random.choice -> 추출해서 이름들, 목록
# 1. st.session_state - n, g가 섞여있음
ss = pd.Series(st.session_state) # 딕셔너리 -> 시리즈
# st.write(ss)
# ss2 = ss[ss != ""]
ss2 = ss[ss.ne("")]
# st.write(ss2)

# str: string 관련된 메소드를 사용할 수 있게 함
n_idx = ss2.index.str.contains('n')
n_data = ss2[n_idx]
# st.write(n_data)

g_idx = ss2.index.str.contains('g')
g_data = ss2[g_idx]
# st.write(g_data)

# n_data를 섞어줄 것임 (비복원으로)
n_rd = np.random.choice(n_data, len(n_data), replace=False)
st.write(n_rd)
g_rd = np.random.choice(g_data, len(g_data), replace=False)
st.write(g_rd)
#2. df 형태로 정리
# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽