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

# sudo docker run -itd -p 8080:8080 yiluxiangbei/aktools
sudo docker run --name aktools -itd -p 8080:8080 yiluxiangbei/aktools

http://82.157.51.152:8080/

sudo docker build -t yiluxiangbei/aktools:zhuzhu -f docker/Dockerfile .
sudo docker push yiluxiangbei/aktools:zhuzhu

sudo docker run -it yiluxiangbei/aktools:zhuzhu python
sudo docker run -it yiluxiangbei/aktools:zhuzhu bash

sudo docker run -it --volume="$(pwd)":/zhuzhu --rm yiluxiangbei/aktools bash
sudo docker run -it --volume="$(pwd)":/zhuzhu --rm yiluxiangbei/aktools:zhuzhu bash

python get_code.py

sudo docker run -ti --privileged --volume="$(pwd)":/ejyy -v $(pwd)/root:/root --rm node:14 bash

docker rm `docker ps -a|grep aktools|  awk '{print $1}'`
docker rmi `docker images|grep none |  awk '{print $3}'`
```