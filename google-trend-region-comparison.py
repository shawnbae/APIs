from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색, keyword, 검색 기간 입력
keyword = "WTO"
period = "now 7-d" # 검색 기간: 최근 7일

# Google Trend 접속
trend_obj = TrendReq()
trend_obj.build_payload(kw_list = [keyword], timeframe=period)

# 지역별 검색 Trend 비교
trend_df = trend_obj.interest_by_region().sort_values(by= keyword, ascending=False)
print(trend_df.head())

# 그래프 출력하기
