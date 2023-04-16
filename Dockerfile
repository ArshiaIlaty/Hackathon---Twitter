FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y python locales python3-pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code

CMD ["hypercorn", "src:main:app", "--bind", "0.0.0.0", "--port", "80"]