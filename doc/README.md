```shell
sudo docker pull registry.cn-shanghai.aliyuncs.com/akfamily/aktools:jupyter
sudo docker run -it registry.cn-shanghai.aliyuncs.com/akfamily/aktools:jupyter python
import akshare as ak
print(ak.__version__)
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
```