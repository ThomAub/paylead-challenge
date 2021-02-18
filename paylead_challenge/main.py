from typing import List

import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from sklearn import metrics
from sklearn.exceptions import NotFittedError
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from paylead_challenge.data_types import DataModel, FeatureVector, Prediction, TrainKPI
from paylead_challenge.views import home

# Creation of the app
api = FastAPI()
api.include_router(home.router)

# Not the best way to do it but works
# This will store our dataset. Everything is lost if server is stop
bdd: pd.DataFrame = pd.DataFrame(
    [],
    columns=["cont_1", "cont_2", "cont_3", "cont_4", "cont_5", "cont_6", "cat_1", "cat_2", "dis_1", "dis_2", "label"],
    dtype=float,
)
api.bdd = bdd

# Same trick to have the model
api.ml_model = LogisticRegression(penalty="l1", solver="liblinear", max_iter=1000)


@api.post("/data/train", response_model=str)
def store_train_data(train_data: List[DataModel]):
    """
    Endpoint to store some training data.

    Args:
        train_data (List[DataModel]): A vector of DataModel

    """
    data_flatten = [entry.flatten() for entry in train_data]
    new_batch = pd.DataFrame().from_dict(data_flatten)
    api.bdd = api.bdd.append(new_batch, ignore_index=True)

    return f"currently {api.bdd.shape[0]} in the database"


@api.get("/model/train", response_model=TrainKPI)
def model_train():
    """Endpoint to launch a training of a model."""
    # A bit arbitrary but we say there is a minimum of 10 examples to make a training.
    number_example = api.bdd.shape[0]
    if number_example < 10:
        raise HTTPException(status_code=500, detail=f"currently {api.bdd.shape[0]} in the database but minimum is 10")

    label = api.bdd.pop("label")
    x_train, x_val, y_train, y_val = train_test_split(api.bdd, label, train_size=0.80)
    api.ml_model.fit(x_train, y_train)

    y_predicted = api.ml_model.predict_proba(x_val).astype(np.int32)
    y = y_val.astype(np.int32)
    y_pred_label = np.argmax(y_predicted, axis=1)

    # metrics
    accuracy = metrics.accuracy_score(y_true=y, y_pred=y_pred_label)
    tn, fp, fn, tp = metrics.confusion_matrix(y, y_pred_label).ravel()

    api.bdd["label"] = label

    return TrainKPI(
        number_example_train=x_train.shape[0],
        number_example_val=x_val.shape[0],
        accuracy=accuracy,
        tp=tp,
        fp=fp,
        fn=fn,
        tn=tn,
    )


@api.post("/model/predict", response_model=Prediction)
def model_predict(test_data: FeatureVector):
    """
    Endpoint to make a prediction with the model. The endpoint `model/train` should have been used before this one.

    Args:
        test_data (FeatureVector): A unit vector of feature

    """
    try:
        y_predicted = api.ml_model.predict_proba(test_data.to_numpy())

    except NotFittedError:

        raise HTTPException(
            status_code=500,
            detail="This LogisticRegression instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.\nUse `model/train` endpoint with 10 examples before",
        )

    y_pred_label = np.argmax(y_predicted, axis=1).astype(np.int32)
    y_pred_score = np.max(y_predicted, axis=1)

    return Prediction(label=y_pred_label, probability=y_pred_score)
