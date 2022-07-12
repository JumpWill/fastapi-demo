
FROM python:3.8-slim

# 2、将当前工作目录设置为 /code
# 这是放置 requirements.txt 文件和应用程序目录的地方
WORKDIR /code
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai'>/etc/timezone
RUN pip install -U pip
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
COPY ./  /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
## 6、运行服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]