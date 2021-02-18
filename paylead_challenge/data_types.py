from typing import Optional

import numpy as np
from pydantic import BaseModel


class FeatureVector(BaseModel):
    cont_1: float
    cont_2: float
    cont_3: float
    cont_4: float
    cont_5: float
    cont_6: float
    cat_1: float
    cat_2: float
    dis_1: float
    dis_2: float

    def to_numpy(self) -> np.ndarray:
        return np.array(
            [
                self.cont_1,
                self.cont_2,
                self.cont_3,
                self.cont_4,
                self.cont_5,
                self.cont_6,
                self.cat_1,
                self.cat_2,
                self.dis_1,
                self.dis_2,
            ]
        ).reshape(1, -1)


class Prediction(BaseModel):
    label: int
    probability: Optional[float]


class DataModel(BaseModel):
    features: FeatureVector
    label: int

    def flatten(self):
        flatten_dict = {key: value for key, value in self.features.dict().items()}
        flatten_dict["label"] = self.label
        return flatten_dict


class TrainKPI(BaseModel):
    number_example_train: int
    number_example_val: int
    accuracy: float
    tp: int
    fp: int
    fn: int
    tn: int
    # confusion_matrix: Tuple[int, int, int, int] = field(init=False)
