FROM python:3.7.2-stretch
# ssh-agent -s

#  ssh-add ~/.ssh/id_rsa
WORKDIR /app

ADD ./app /app/


RUN pip install -r requirements.txt



CMD ["uwsgi", "app.ini"]

