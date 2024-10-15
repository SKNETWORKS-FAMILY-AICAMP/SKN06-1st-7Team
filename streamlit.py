import pandas as pd  # 데이터 처리 라이브러리 임포트
import streamlit as st  # 웹 애플리케이션 라이브러리 임포트
import altair as alt  # 데이터 시각화 라이브러리 임포트
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 웹 페이지 제목 설정
st.title('서울시 등록 자동차 대수 & 자치구별 자동차 사고 횟수')  

# LTA의 데이터셋 로드
df_rgst_by_month = pd.read_csv('자동차등록수.csv')  # CSV 파일에서 데이터프레임 생성
df_car_acc_by_month = pd.read_csv('교통사고.csv') # csv 파일에서 dnjfquf

# 선택 입력 위젯 준비
gu_list = df_rgst_by_month.groupby('district').sum().sort_values(by=['number'], ascending=False).reset_index()
acc_list = df_car_acc_by_month.groupby('district').sum().sort_values(by=['number'], ascending=False).reset_index()

# 월 목록 생성
month_df = pd.to_datetime(df_rgst_by_month['month']).drop_duplicates().sort_values()
month_df2 = pd.to_datetime(df_car_acc_by_month['month']).drop_duplicates().sort_values()

# 슬라이더 바 사용
start_month, end_month = st.select_slider(
    '기간을 선택해주세요.',  # 슬라이더의 설명
    options=month_df.apply(lambda x: x.strftime("%Y-%m")).tolist(),  # 슬라이더에서 선택할 수 있는 연도 목록
    value=(month_df.min().strftime("%Y-%m"), month_df.max().strftime("%Y-%m"))  # 기본값 설정
)

# 문자열을 datetime으로 변환하여 필터링에 사용
start_month_date = datetime.strptime(start_month, "%Y-%m")
end_month_date = datetime.strptime(end_month, "%Y-%m")

# 선택된 연도 범위에 따라 데이터 필터링
column_data = df_rgst_by_month[(pd.to_datetime(df_rgst_by_month['month']) >= start_month_date) & 
                               (pd.to_datetime(df_rgst_by_month['month']) <= end_month_date)]
# car_accident
column_data2 = df_car_acc_by_month[(pd.to_datetime(df_car_acc_by_month['month']) >= start_month_date) & 
                               (pd.to_datetime(df_car_acc_by_month['month']) <= end_month_date)]

# Streamlit에서 제목 설정
st.header(f'기간{start_month}에서부터 {end_month} 사이를 살펴봅니다.')  # 비교할 월 제목 설정

# 행렬을 2x5로 나누기 위한 준비
num_rows = 2
num_columns = 5
rows = [st.columns(num_columns) for _ in range(num_rows)]  # 2행 x 5열의 구조 생성


# 모든 구의 차이와 마지막 수치를 계산하여 리스트에 저장
district_data = []
for gu in gu_list['district']:
    last_row = column_data[column_data['district'] == gu].pivot(index='month', columns='district', values='number').fillna(0).iloc[-1:]
    start_row = column_data[column_data['district'] == gu].pivot(index='month', columns='district', values='number').fillna(0).iloc[0:]
    
    diff = last_row.iloc[0, 0] - start_row.iloc[0,0]
    last_metric = last_row.iloc[0, 0]
    
    district_data.append((gu, int(last_metric), int(diff)))

# 차이(diff)를 기준으로 정렬
district_data.sort(key=lambda x: x[2], reverse=True)

# 상위 6개와 하위 6개 선택
top_5 = district_data[:5]
bottom_5 = district_data[-5:]

# 선택된 10개 구 표시
selected_districts = top_5 + bottom_5

index_x = 0
for gu, last_metric, diff in selected_districts:
    row = index_x // num_columns
    col = index_x % num_columns
    rows[row][col].metric(label=gu, value=last_metric, delta=diff)
    index_x += 1

st.write('\n')  # 띄우기
st.write('\n')  

# 다중 선택 사용
multiselect_option = st.multiselect(
    '자치구 어디에 관심이 있으신가요?',  # 선택 질문
    gu_list['district'],  # 선택할 구 목록
    key='multiselect_option'
)

st.write('\n')  # 띄우기
st.write('\n')  

# 브랜드와 연도로 필터링 & 사고 수
filterbybrand_data = column_data[column_data['district'].isin(multiselect_option)]  
filterbybrand_data2 = column_data2[column_data2['district'].isin(multiselect_option)]  

# 첫 번째 차트
st.caption('서울시 내에 등록된 자치구별 차량 수와 자치구별 자동차 사고 수')  # 차트 설명

# Altair를 사용해 선 그래프 생성
c = alt.Chart(filterbybrand_data, title = '자동차 등록수').mark_line().encode(
    x='month:T', y='number:Q', color='district:N', strokeDash='district:N'
)

# 사고 수
c2 = alt.Chart(filterbybrand_data2, title = '사고 횟수').mark_line().encode(
    x='month:T', y='number:Q', color='district:N', strokeDash='district:N'
)

## 그래프 가로 버전
# combined_chart = c | c2
# st.altair_chart(combined_chart, use_container_width=True)

# 그래프 세로 버전 
st.altair_chart(c, use_container_width=True)  # 차트를 웹 페이지에 표시
st.altair_chart(c2, use_container_width=True)  # 차트를 웹 페이지에 표시

st.write('made by. Kang & Kim & Jo')  # 선택된 월 출력