
# Pseudo App
This demo app is part of the document's pseudonymization effort lead at [Etalab's](https://www.etalab.gouv.fr/) [Lab IA](https://github.com/etalab-ia/).  Other Lab IA projects can be found at the [Lab IA](https://github.com/etalab-ia).

#### Project Status: [Active]

## Intro/Objectives
The purpose of this repo is to provide a quick demo to the pseudonymization tool we developped. The larger goal of the pseudonymization project is to help France's Conseil d'État open their Justice decisions to the general public, as required by the law. More info about pseudonymization and this project can be found in our French pseudonymization guide [here](https://guides.etalab.gouv.fr/pseudonymisation/). Behind this web site, there is an API that does the job of text tagging and pseudonymization.


### Methods Used
* Natural Language Processing: Information Extraction : Named Entity Recognition
* Natural Language Processing: Language Modelling / Feature Learning: Word embeddings
* Machine Learning: Deep Learning: Recurrent Networks: BiLSTM+CRF

### Technologies
* Python
* Flair, sacremoses
* Dash
* SQLite
* Pandas

## Demo Description

The demo consists in four tabs: 

1. Introduction of the project:  a brief insight into our pseudonymisation project,
2. Upload of a document to be pseudonymized: allows for an imageless .doc, .docx, or .txt file to be uploaded (up to 100 kB)  
3. Comparison of volume of training data vs annotation performance:  we try to answer the question how much data do I need to get decent results?
4. API Stats: the use stats of the API that actually does the work.

This demo depends by default on the [pseudo API](https://github.com/psorianom/pseudo_api). The API is automatically pulled from its repo in the `docker-compose` file.

You do need to train a NER model with the [Flair library](https://github.com/flairNLP/flair). Unfortunately, we cannot share nor the model nor the data it was trained on as it contains non-public information.

## Getting Started
The easiest way to test this application is by creating a Docker container.
1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Add the path of the local model to the `.env` file. Note that you could also pass this env var to the app directly and you would not need run the API.
3. Launch the wrapper bash file `run_docker.sh`. This file will clean and rebuild the required Docker containers by calling `docker-compose.yml`.
4. Go to `localhost/pseudo/`


## Project Deliverables
* This Demo 
* [Pseudonymization API](https://github.com/psorianom/pseudo_api)
* [Pseudonymization Guide](https://guides.etalab.gouv.fr/pseudonymisation/)


## Contact
* Feel free to contact [@psorianom](https://github.com/psorianom/) or other [Lab IA](https://github.com/etalab-ia/) team members with any questions or if you are interested in contributing!
