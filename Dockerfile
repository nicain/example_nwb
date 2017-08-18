#
# dipde miniconda Dockerfile
#
# https://github.com/NeurodataWithoutBorders/pynwb
# http://pynwb.readthedocs.io/en/latest/index.html

# Pull base image.
FROM continuumio/miniconda:latest

# Allows plotting tests
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx
USER root
SHELL ["/bin/bash", "-c"]

RUN conda update -y conda
RUN conda create -n python27 python=2.7
RUN source activate python27
WORKDIR /
RUN git clone https://github.com/nicain/pynwb.git
WORKDIR /pynwb
RUN git checkout feature/table_writer_dataset23

RUN pip install -r 'requirements.txt'
RUN conda install -y pandas matplotlib numpy scipy PIL statsmodels scikit-image
RUN pip install allensdk
RUN python setup.py build
RUN python setup.py install
RUN python test.py
