import akshare as ak
import pandas as pd
import numpy as np
import os

"""
获取A股所有股票的代码
使用stock_info_a_code_name(),反馈数据格式详细参见akshare官网
"""
StockList = ak.stock_info_a_code_name()
#StockList返回的股票代码是“000001”，“000002”这样的格式
#但是stock_zh_a_daily（）函数中，要求代码的格式为“sz000001”，或“sh600001”
#即必须有sz或者sh作为前序
#因此，通过for循环对股票代码code进行格式变换
"""
for i in range(0, len(StockList)):
    temp = StockList.iloc[i,0]
    if temp[0] == "6":
        temp="sh" + temp
    if temp[0] == "0":
        temp = "sz" + temp
    if temp[0] == "3":
        temp = "sz" + temp
    StockList.iloc[i, 0] = temp
"""

#通过txt形式保存数据，先检测是否存在文件。
#若存在，则在更新股票列表时，先将原有文件删除，再重建文件。
if os.path.exists("./stockList.csv"):
    os.remove("./stockList.csv")
StockList.to_csv("./stockList.csv", sep=",", index=False, header=True)
#将原有表格删除后，更新原有数据

"""
下一步，根据原有的股票代码数据，读取历史数据
"stock_zh_a_hist"  # A 股日频率数据-东方财富
"stock_zh_ah_daily"  # 获取 A+H 股历史行情数据(日频)
"stock_zh_a_daily"  # 获取 A 股历史行情数据(日频)
"stock_zh_kcb_daily"  # 获取科创板历史行情数据(日频)
"option_sina_cffex_hs300_daily"  # 沪深300期权历史行情-日频
 "option_sina_sse_daily"  # 上交所期权日频数据
"""