# 하와이 인구
hi_population = 1441553

# 대한민국 인구
kor_population = 51815808

# 비율 = 대한민국 인구 / 하와이 인구
actual_rate = kor_population / hi_population

print("=" * 50)
print(f"** 하와이 인구: {hi_population:,} 명")
print(f"** 대한민국 인구: {kor_population:,} 명")
print("-" * 50)
print(f"파일 데이터 기반 실제 인구 비율 (대한민국/하와이): {actual_rate:.4f}")

rate_from_sample02 = 20.13
kor_population_derived = rate_from_sample02 * hi_population
print(f"평균:{kor_population_derived: .4f}")
print("-" * 50)