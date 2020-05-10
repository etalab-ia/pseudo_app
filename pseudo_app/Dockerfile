FROM continuumio/miniconda3

WORKDIR usr/src/pseudo_app
RUN apt-get update && apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
ADD environment.yml environment.yml

RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/dash_pseudo_app/bin:$PATH
RUN /bin/bash -c "source activate dash_pseudo_app"
COPY . .
