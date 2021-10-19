FROM ubuntu:focal

ENV PATH=/opt/octoflow/venv/bin:$PATH
ENV PYTHONPATH=$PYTHONPATH:/opt/octoflow

# Octoflow Base Image
# Base image to be compatible with FastAPI, Airflow, and Jupyter integration

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3.8 python3.8-dev python3.8-distutils python3.8-venv \
    && rm -rf /var/lib/apt/lists/*

USER root

ENV PATH=/opt/octoflow/venv/bin:$PATH
ENV PYTHONPATH=$PYTHONPATH:/opt/octoflow

WORKDIR /opt/octoflow

COPY src/ /opt/octoflow/src
COPY setup.py /opt/octoflow/setup.py
COPY requirements.txt /opt/octoflow/requirements.txt
COPY entrypoint.sh /opt/octoflow/entrypoint.sh

RUN chown -R 777 /opt/octoflow
RUN chmod +x /opt/octoflow/entrypoint.sh

RUN python3 -m venv /opt/octoflow/venv \
    && pip --disable-pip-version-check --no-cache-dir install -r requirements.txt

RUN python3 setup.py build \
    && python3 setup.py install

ENTRYPOINT [ "/opt/octoflow/entrypoint.sh" ]