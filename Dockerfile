
FROM python:3.8-slim

WORKDIR /code
RUN   cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai'>/etc/timezone \
   && pip install -U pip \
   && pip config set global.index-url http://mirrors.aliyun.com/pypi/simple \
   && pip config set install.trusted-host mirrors.aliyun.com \
   && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./  /code

## 6、运行服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
