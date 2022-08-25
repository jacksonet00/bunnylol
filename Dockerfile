FROM python:3.8

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /usr/src/app

CMD ["python3", "manage.py"]

EXPOSE 5000