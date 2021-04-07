from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword1 = "apple iphone"
keyword2 = "samsung galaxy"
period = "today 5-y" # 검색 기간 5

# Google Trend 접속 및 데이터 탑재
trend_obj = TrendReq()
trend_obj.build_payload(kw_list = [keyword1, keyword2], timeframe=period)
trend_df = trend_obj.interest_over_time()

# 그래

