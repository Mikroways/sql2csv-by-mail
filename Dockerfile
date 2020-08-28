FROM python:3
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get install -y zip && pip install -r requirements.txt
CMD [ "/app/sendmail" ]
