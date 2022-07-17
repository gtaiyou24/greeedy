FROM python:3.9

MAINTAINER gtaiyou24 gtaiyou24@gmail.com

ENV TZ=Asia/Tokyo

ARG project_dir=/app/
COPY . $project_dir
COPY requirements.txt $project_dir
WORKDIR $project_dir

# ライブラリをインストール
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

# uvicornのサーバーを立ち上げる
#CMD ["uvicorn", "start_api:api", "--host", "0.0.0.0", "--reload"]
