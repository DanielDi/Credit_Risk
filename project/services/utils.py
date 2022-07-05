from enum import Enum
import numpy as np
import pandas as pd
from models.enums import PredictionModel


def feature_list(enum: Enum) -> tuple[list, list]:
    readable_features = [feature.value for feature in enum]
    orig_features = [feature.name.lower() for feature in enum]
    return orig_features, readable_features

def feature_equivalence(enum: Enum) -> list[dict]:
    orig_features, readable_features = feature_list(enum)
    return [{'label': readable, 'value': orig} for orig, readable in zip(orig_features, readable_features)]

def model_list() -> list:
    return [model.value for model in PredictionModel]

def read_feather_db(file_name: str='mini_db.feather') -> pd.DataFrame:
    df = pd.read_feather(file_name)
    df = df.drop(columns=['index'], axis=1)
    clipped_df = remove_extreme_outliers(df)
    return clipped_df

def remove_extreme_outliers(df: pd.DataFrame, quantiles: tuple=(0.01, 0.99)) -> pd.DataFrame:
    cols = df.select_dtypes(np.number).columns
    thresh = df[cols].quantile(quantiles)
    clipped_df = df.copy()
    clipped_df[cols] = df[cols].clip(lower=thresh.iloc[0], upper=thresh.iloc[1], axis=1)
    return clipped_df