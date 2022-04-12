ARG BASE_IMAGE=nvcr.io/nvidia/pytorch:22.01-py3

FROM ${BASE_IMAGE}

RUN pip install Pillow
RUN pip install boto3
RUN pip install seaborn
