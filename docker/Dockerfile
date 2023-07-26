FROM python:3.11

# 升级 pip 到最新版
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/

# 新增 gunicorn 安装，提升并发和并行能力
RUN pip install --no-cache-dir akshare fastapi uvicorn gunicorn -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
RUN pip install --no-cache-dir aktools -i https://mirrors.aliyun.com/pypi/simple/ --upgrade

WORKDIR /zhuzhu
