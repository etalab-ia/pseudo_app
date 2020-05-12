FROM continuumio/miniconda3

WORKDIR usr/src/pseudo_app
RUN apt-get update && apt-get install antiword
ADD environment.yml environment.yml

RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/dash_pseudo_app/bin:$PATH
RUN /bin/bash -c "source activate dash_pseudo_app"
COPY . .
