import matplotlib.pyplot as plt
import pandas as pd

# 1. 데이터 불러오기
file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

# 2. 나이가 '35-44 years old'인 행만 필터링
target_age = '35-44 years old'
df_filtered = df_raw[df_raw['Age'] == target_age]

# 3. 언어 컬럼 선택
COL_LANG = 'LanguageHaveWorkedWith'
ds_data = df_filtered[COL_LANG]

# 결측치 제거 (문자열 조작 전처리)
ds_data = ds_data.dropna()

# 4. 데이터 전처리
# 세미콜론으로 분리
ds_data = ds_data.str.split(';')

# 리스트를 행으로 펼치기
ds_data = ds_data.explode()

# 그룹바이로 개수 세기
ds_data = ds_data.groupby(ds_data).size()

# 5. 상위 5개 선정 및 파이 차트 생성
top_5_data = ds_data.nlargest(5)

plt.figure(figsize=(10, 10))
top_5_data.plot.pie(autopct='%1.2f%%')
plt.title(f'Top 5 Languages for Developers ({target_age})')
plt.ylabel('')  # y축 라벨 제거
plt.tight_layout()

# 6. 차트 이미지 저장
plt.savefig('top5_languages_35_44.png')

# 결과 출력
print(top_5_data)