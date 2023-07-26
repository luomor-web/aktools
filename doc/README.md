```shell
股票代码 数据
sudo docker pull registry.cn-shanghai.aliyuncs.com/akfamily/aktools:jupyter
sudo docker run -it registry.cn-shanghai.aliyuncs.com/akfamily/aktools:jupyter python
import akshare as ak
print(ak.__version__)
1.7.35
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="")
print(stock_zh_a_hist_df)

import akshare as ak
stock_info_a_code_name_df = ak.stock_info_a_code_name()
print(stock_info_a_code_name_df)

stock_info_sz_name_code = ak.stock_info_sz_name_code()
print(stock_info_sz_name_code)

stock_info_sh_name_code = ak.stock_info_sh_name_code()
print(stock_info_sh_name_code)

stock_info_sh_df = ak.stock_info_sh_name_code(indicator="主板A股")
print(stock_info_sh_df)

"stock_info_sz_name_code" # 深证证券交易所股票代码和简称
"stock_info_sh_name_code" # 上海证券交易所股票代码和简称
"stock_info_a_code_name" # A 股股票代码和简称
https://akshare.akfamily.xyz/

sudo docker build -t yiluxiangbei/aktools -f Dockerfile .
sudo docker push yiluxiangbei/aktools

sudo docker run -it yiluxiangbei/aktools python
import akshare as ak
print(ak.__version__)
1.10.71

import akshare as ak
stock_info_a_code_name_df = ak.stock_info_a_code_name()
print(stock_info_a_code_name_df)

stock_info_sz_name_code = ak.stock_info_sz_name_code()
print(stock_info_sz_name_code)

stock_info_sh_name_code = ak.stock_info_sh_name_code()
print(stock_info_sh_name_code)
# python list to csv
# import pandas as pd
import csv
 
# path为输出路径和文件名，newline=''是为了不出现空行
csvFile = open("/tmp/test.csv", "w+", newline='')
# name为列名
name = ['code', 'name']
try:
    writer = csv.writer(csvFile)
    writer.writerow(name)
    # stock_info_a_code_name_df为list类型
    for i in range(len(stock_info_a_code_name_df)):
        writer.writerow(stock_info_a_code_name_df[i])
finally:
    csvFile.close()

sudo docker run -it yiluxiangbei/aktools --volume="$(pwd)":/zhuzhu bash
sudo docker run -it yiluxiangbei/aktools python doc/get_code.py
```