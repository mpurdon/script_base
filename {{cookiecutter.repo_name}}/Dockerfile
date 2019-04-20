ARG PYTHON_VERSION=3.7.3-alpine

FROM python:${PYTHON_VERSION} as python_build_container

ENV PYTHONUNBUFFERED 1

RUN mkdir /install
WORKDIR /install

COPY requirements*.txt /

#RUN pip install --upgrade --install-option="--prefix=/install" pip==18.1 setuptools

RUN pip install --install-option="--prefix=/install" -r /requirements_dev.txt

FROM python_build_container as python_build

COPY --from=python_build_container /install /usr/local
COPY .. /app

WORKDIR /app

#CMD python main.py
