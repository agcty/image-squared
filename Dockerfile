FROM python:3.7.2-alpine3.8
#COPY requirements.txt ./code/
WORKDIR /images/

RUN apk update && apk upgrade

#--virtual groups build packages with the name build-dependencies to remove later
RUN apk add --update --no-cache --virtual \
    build-dependencies \
    python3-dev \
    build-base \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev 
# && pip install -r requirements.txt
# && apk del build-dependencies

RUN apk add imagemagick

COPY . /code/

CMD ["sh"]
# RUN echo "yolo" >> /app/test.txt
# CMD ["scrapy", "runspider", "scrapeprice.py", "-t", "csv", "-o", "-", ">", "/app/prices.csv"]