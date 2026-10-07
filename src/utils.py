import os
import dill
import pickle
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path != "":
            os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train, models, param):
    try:
        report = {}

        for model_name, model in models.items():
            para = param[model_name]

            gs = GridSearchCV(model,para,cv=3) # ,n_jobs=n_jobs,verbose=verbose,refit=refit
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train) # Train model

            report[model_name] = (gs.best_score_, gs.best_params_)

        return report
    except Exception as e:
        raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
