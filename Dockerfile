FROM python3.7

RUN apt-get -y update
RUN apt-get -y install libpq-dev
RUN apt-get -y install nano
RUN apt-get -y install gcc

RUN pip install --upgrade pip
RUN pip install alembic
RUN pip install psycopg2

RUN command cd /root && mkdir demo
WORKDIR /root/demo
ENV PYTHONPATH=/root/demo
