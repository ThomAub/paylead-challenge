# Paylead technical challenge

* [Technical decisions](#technical-decisions)
* [Installation](#installation)
* [Feature tracker](#feature-tracker)

We want to make an API in order to interact with our dataset and a machine learning model. 

We have already a set of data describing our problem about 25K entry. 
Each entry has 10 features. Jugging by their name and a quick look on the data itself there is: 
- 6 countinous features. $CONT_i$ 
- 2 categorical feature but it seems already encoded
- 2 discrete feature but it seems already encoded
- 1 label 0 or 1, binary classification 


## Technical decisions

Looking at the time constraint and the features it's not really possible to implement them all. 
Going for 1, 2, 3 in that order could be possible. 

DB will be in memory DB because there is not really the time for something else.
Model will be a scikit-learn linear model.
We can play a bit on the seperate script to find a good set of model and hyper parameters or maybe let the user choose one ? 

API will be implemented with FastAPI mostly because i wanted to try it a bit and offer automated docs and validate input type.

Docs and tests will be less present because real test of api would take a bit too long. At least we have pydantic that will help for the type checking. 

For each feature, 1 2 and 3, an endpoint will be created.
- 1 -> "/data/train" with a POST
- 2 -> "/model/train" with a GET
- 3 -> "/model/test" with a GET

Each of the endpoint and the rest of the api is available at "/docs". 

Please use the `Try it out` button to easily make request to the API. It will create the curl command for you. 

1 -> Using a pandas Dataframe for in memory storage. Global access to the DB but should not be a problem no async functions.

2 -> Model training is similar than in the script `scripts/train_model.py`. Note with 80/20 split model achieves 95% accuracy. 

3 -> Simple inference using a feature vector and checking if the model is already trained. 

## Installation

Check the README for more info but you can choose to install:

- virtual environement with poetry
- docker with `dev.dockerfile.build.sh` and `dev.dockerfile.run.sh` in `.devcontainer/`. 

## Feature tracker

[X] 1/ Je peux poster des labels de train (sous forme de batch donc plusieurs lignes à la fois) et les storer

[X] 2/ Je peux lancer le train d’un modèle sur l’ensemble des labels storés et obtenir en retour qqes KPIs tels que: 
- Le nombre de labels utilisés pour le train
- la matrice de confusion (bonnes prédictions, faux positifs, faux négatifs)

[X] 3/ Je peux poster des labels (de test) unitairement et obtenir en retour la prédiction 1 ou 0 avec la probabilité

[] 4/ Je peux fetcher l’historique des KPIs de train sur les différents train qui ont eu lieu (ce qui permet d’avoir l’évolution du nombre de labels ou de la précision par exemple)

[] 5/ Je peux lancer automatiquement le train d’un modèle après chaque post de l’étape 1/

[] 6/ Je peux refuser d’utiliser un modèle pour la prédiction lorsque la précision est inférieure à un seuil donné

[] 7/ Je peux supprimer des labels de train

[] 8/ Je peux labelliser une prédiction obtenue via 3/ pour l’ingérer ensuite en train
