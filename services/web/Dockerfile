FROM spark
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./project/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./project /usr/src/app